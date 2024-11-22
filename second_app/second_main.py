from typing import Annotated

from fastapi import FastAPI, Body

ALLOWED = set('0123456789+-/%*()^<>|~& ')

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/ping/")
def read_root():
    return {"PING": "PONG"}


@app.post("/solve/")
def read_item(expression: Annotated[str, Body()]):
    if not expression:
        return {}

    for char in expression:
        if char not in ALLOWED:
            return {"error": "not allowed expression"}
    try:
        return {"result": eval(expression.strip(' \"\''))}
    except SyntaxError:
        return {"error": "wrong expression"}
    except:
        return {"error": "something went wrong"}
