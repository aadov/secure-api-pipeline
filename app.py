from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Secure API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )

@app.get("/db-check")
def db_check():
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.close()
        return {"db": "ok"}
    except Exception as e:
        return {"db": "error", "details": str(e)}
    finally:
        if conn:
            conn.close()
