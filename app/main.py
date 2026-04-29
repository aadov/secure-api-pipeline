from fastapi import FastAPI
from sqlalchemy import create_engine, text
import os

app = FastAPI(title="Secure API Pipeline")

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:secret@db:5432/securedb")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"db": "connected"}
    except Exception as e:
        return {"db": "error", "detail": str(e)}
