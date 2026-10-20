from fastapi import FastAPI

app = FastAPI(title="Health API", version="1.0.0")

@app.get("/")
def root():
    return {
        "app": "health-api",
        "version": "1.0.0",
        "message": "Hello from Health API!",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready():
    return {"status": "ready"}

