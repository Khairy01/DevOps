import redis
from fastapi import FastAPI

app = FastAPI()

redis_client = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)

@app.get("/visited")
def read_user_visits():
    visits = redis_client.incr("visits")
    return {"Hellooooo": "DIC2!", "visits": visits}


@app.get("/users")
def users():
    return {"user": []}