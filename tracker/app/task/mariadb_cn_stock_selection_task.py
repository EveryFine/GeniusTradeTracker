# -*- coding: utf-8 -*-
"""
Task to fetch last 7 days from MariaDB cn_stock_selection and insert into Postgres.
"""
from datetime import date, timedelta
import traceback

import pymysql

from app.common.log import log
from app.core.conf import settings
from app.crud.crud_cn_stock_selection import upsert_cn_stock_selection_rows

# Columns that are boolean in Postgres and need conversion from tinyint/bit
BOOLEAN_FIELDS = {
    'macd_golden_fork', 'macd_golden_forkz', 'macd_golden_forky',
    'kdj_golden_fork', 'kdj_golden_forkz', 'kdj_golden_forky',
    'break_through', 'low_funds_inflow', 'high_funds_outflow',
    'breakup_ma_5days', 'breakup_ma_10days', 'breakup_ma_20days', 'breakup_ma_30days', 'breakup_ma_60days',
    'long_avg_array', 'short_avg_array', 'upper_large_volume', 'down_narrow_volume',
    'one_dayang_line', 'two_dayang_lines', 'rise_sun', 'power_fulgun', 'restore_justice',
    'down_7days', 'upper_8days', 'upper_9days', 'upper_4days', 'heaven_rule', 'upside_volume',
    'bearish_engulfing', 'reversing_hammer', 'shooting_star', 'evening_star', 'first_dawn', 'pregnant',
    'black_cloud_tops', 'morning_star', 'narrow_finish', 'limited_lift_f6m', 'limited_lift_f1y',
    'limited_lift_6m', 'limited_lift_1y', 'directional_seo_1m', 'directional_seo_3m', 'directional_seo_6m',
    'directional_seo_1y', 'recapitalize_1m', 'recapitalize_3m', 'recapitalize_6m', 'recapitalize_1y',
    'equity_pledge_1m', 'equity_pledge_3m', 'equity_pledge_6m', 'equity_pledge_1y',
    'is_issue_break', 'is_bps_break', 'now_newhigh', 'now_newlow',
    'high_recent_3days', 'high_recent_5days', 'high_recent_10days', 'high_recent_20days', 'high_recent_30days',
    'low_recent_3days', 'low_recent_5days', 'low_recent_10days', 'low_recent_20days', 'low_recent_30days',
    'win_market_3days', 'win_market_5days', 'win_market_10days', 'win_market_20days', 'win_market_30days'
}


def execute_sync_cn_stock_selection_last_3_days() -> int:
    """Fetch last 7 days from MariaDB and insert missing rows into Postgres.

    Returns number of rows processed (attempted inserts).
    """
    if not settings.MARIADB_HOST or not settings.MARIADB_USER or not settings.MARIADB_DB:
        log.error("MariaDB settings not configured. Skipping sync.")
        return 0

    end_date = date.today()
    start_date = end_date - timedelta(days=3)
    rows = []

    conn = None
    try:
        conn = pymysql.connect(host=settings.MARIADB_HOST,
                               port=int(settings.MARIADB_PORT),
                               user=settings.MARIADB_USER,
                               password=settings.MARIADB_PASSWORD or "",
                               database=settings.MARIADB_DB,
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

        with conn.cursor() as cursor:
            sql = "SELECT * FROM cn_stock_selection WHERE `date` >= %s"
            cursor.execute(sql, (start_date,))
            rows = cursor.fetchall()

        if not rows:
            log.info("No rows fetched from MariaDB for last 3 days.")
            return 0
        else:
            log.info(f"Found {len(rows)} rows for last 3 days.")

        # normalize boolean/bit fields and keys if necessary
        normalized = []
        for r in rows:
            newr = {}
            for k, v in r.items():
                # pymysql may return bytearray for BIT columns; convert to int first
                if isinstance(v, (bytes, bytearray)):
                    try:
                        int_val = int.from_bytes(v, byteorder='big')
                    except Exception:
                        newr[k] = v
                        continue
                    if k in BOOLEAN_FIELDS:
                        newr[k] = bool(int_val)
                    else:
                        newr[k] = int_val
                elif isinstance(v, int):
                    if k in BOOLEAN_FIELDS:
                        newr[k] = bool(v)
                    else:
                        newr[k] = v
                elif isinstance(v, str) and v in ('0', '1'):
                    # sometimes tinyint may come as '0'/'1'
                    if k in BOOLEAN_FIELDS:
                        newr[k] = bool(int(v))
                    else:
                        newr[k] = v
                else:
                    newr[k] = v
            normalized.append(newr)

        inserted = upsert_cn_stock_selection_rows(normalized)
        log.info(f"Sync cn_stock_selection: fetched {len(rows)} rows, attempted insert {inserted} rows")
        return inserted

    except Exception as e:
        log.error(f"Error syncing cn_stock_selection: {e}\n{traceback.format_exc()}")
        return 0
    finally:
        if conn:
            conn.close()
