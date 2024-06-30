## 数据库初始化流程
### 1. 使用SQLModel定义model类
```python
class ArtistBase(SQLModel):
    name: str = Field(max_length=120, description='名称')

class Artist(ArtistBase, table=True):
    """artist表"""
    artist_id: int | None = Field(default=None,primary_key=True, description='id')
```
### 2. 在fastapi项目启动过程中初始化数据库表
```python
@app.on_event("startup")
def on_startup():
    create_db_and_tables()
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
```
### 3. 使用update接口更新数据