# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message1": "Netbook1 Codium FastAPI 🚀", "message2": "Netbook2 Codium FastAPI 🚀"}
