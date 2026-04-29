from fastapi import FastAPI

app = FastAPI(title="Secure API Pipeline")

@app.get("/health")
def health_check():
    return {"status": "ok"}
