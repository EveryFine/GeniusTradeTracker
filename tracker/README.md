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

### 4. 使用Dockerfile编译镜像并启动
```shell
cd tracker
docker build -t genius-trade-tracker:v0.3 .
docker container run -d --name tradetrackermain -p ${{ env.TARGET_SERVICE_PORT }}:13180 --link ${{ env.POSTGRES_CONTAINER_NAME }}:${{ env.POSTGRES_CONTAINER_NAME }} --net=${{ env.POSTGRES_CONTAINER_NETWORK }} -e POSTGRES_HOST=${{ env.POSTGRES_CONTAINER_NAME }} -e POSTGRES_PORT=${{ env.POSTGRES_PORT }} -e POSTGRES_USER=${{ env.POSTGRES_USER }} -e POSTGRES_PASSWORD=${{ env.POSTGRES_PASSWORD }} -e POSTGRES_DB=${{ env.POSTGRES_DB }} genius-trade-tracker:v0.3

docker container run -d --name trade-tracker -p 23180:13180 \
 --env-file .env \
 --link finstore_postgres:finstore_postgres \
 --net="local_default" \
 -e POSTGRES_HOST='finstore_postgres' \
 genius-trade-tracker:v0.3

```
编译好的镜像
ghcr.io/everyfine/geniustradetracker/geniustradetracker:main-00dfa83
```shell
docker container run -d --name trade-tracker -p 23180:13180 \
 --env-file .env \
 --link finstore_postgres:finstore_postgres \
 --net="local_default" \
 -e POSTGRES_HOST='finstore_postgres' \
 ghcr.io/everyfine/geniustradetracker/geniustradetracker:main-00dfa83
```