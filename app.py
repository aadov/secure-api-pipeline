from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Secure API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}
