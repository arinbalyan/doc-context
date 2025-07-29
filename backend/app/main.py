from fastapi import FastAPI
from app.api.v1 import webhook

app = FastAPI()

app.include_router(webhook.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the HackRx 6.0 API"}
