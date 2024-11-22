from fastapi import FastAPI, Body
from requests import get, post
from typing import Annotated

app = FastAPI()


def from_api(path, data=None):
    result = get(f'http://calculator/{path}', data=data, headers={'Content-Type': 'text/plain'}).json()
    if result is None:
        return {"error": "API is not available"}
    return result


@app.get("/")
def read_root():
    return from_api('')


@app.get("/ping/")
def read_root():
    return from_api('ping')


@app.get("/solve/")
def read_item(expression: Annotated[str, Body()]):
    return from_api('solve', expression)
