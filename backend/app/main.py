import os
from fastapi import FastAPI
from app.api.v1 import webhook
import uvicorn

app = FastAPI()

app.include_router(webhook.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the HackRx 6.0 API"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
