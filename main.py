# main.py
from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "Hello": "World",
        "message1": "Netbook1 Codium FastAPI 🚀",
        "message2": "Netbook2 Codium FastAPI 🚀"
        }


# HTTP request by path /items/{item_id}
# Request example:
# http://127.0.0.1:8000/items/42?q=The_Ultimate_Question_of_Life,_the_Universe,_and_Everything.
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

