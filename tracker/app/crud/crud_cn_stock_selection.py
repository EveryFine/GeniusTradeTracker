from typing import List, Dict, Any

from sqlalchemy import text
from sqlalchemy.exc import IntegrityError

from app.core.db import engine


def upsert_cn_stock_selection_rows(rows: List[Dict[str, Any]]) -> int:
    """Insert rows into Postgres cn_stock_selection table while avoiding duplicates.

    Strategy:
    1. If possible, do a batch SELECT for existing (date, code) pairs within the date range
       of incoming rows and skip those prior to inserting. This prevents duplicates even
       when the table lacks a unique constraint.
    2. Still catch `IntegrityError` per-insert as a fallback for race conditions.
    Returns number of successful inserts.
    """
    if not rows:
        return 0

    # gather date range from rows
    dates = sorted({r['date'] for r in rows if r.get('date') is not None})
    if not dates:
        # no date info -> fall back to naive insert with integrity handling
        inserted = 0
        with engine.begin() as conn:
            for r in rows:
                cols = ", ".join(r.keys())
                vals = ", ".join(":" + k for k in r.keys())
                sql = f"INSERT INTO cn_stock_selection ({cols}) VALUES ({vals})"
                try:
                    conn.execute(text(sql), r)
                    inserted += 1
                except IntegrityError:
                    continue
        return inserted

    min_date, max_date = dates[0], dates[-1]

    # fetch existing keys in that date range
    existing_keys = set()
    sel_sql = text("SELECT date, code FROM cn_stock_selection WHERE date BETWEEN :min_date AND :max_date")
    with engine.begin() as conn:
        res = conn.execute(sel_sql, {"min_date": min_date, "max_date": max_date})
        for row in res:
            # SQLAlchemy Row may be a mapping or a tuple depending on driver/version
            try:
                # preferred: mapping access
                mapping = row._mapping
                d = mapping['date']
                c = mapping['code']
            except Exception:
                try:
                    d = row[0]
                    c = row[1]
                except Exception:
                    # skip if we can't parse
                    continue
            existing_keys.add((d, c))

    # filter rows to only those not present
    to_insert = [r for r in rows if (r.get('date'), r.get('code')) not in existing_keys]

    inserted = 0
    with engine.begin() as conn:
        for r in to_insert:
            cols = ", ".join(r.keys())
            vals = ", ".join(":" + k for k in r.keys())
            sql = f"INSERT INTO cn_stock_selection ({cols}) VALUES ({vals})"
            try:
                conn.execute(text(sql), r)
                inserted += 1
            except IntegrityError:
                # race or unexpected integrity error; skip
                continue

    return inserted
