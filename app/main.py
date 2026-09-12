from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(
    title="SecureCloud API",
    version="1.0.0",
    description="Production-style DevSecOps demonstration application",
)


@app.get("/")
def root():
    return {
        "application": "SecureCloud API",
        "version": "1.0.0",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/ready")
def ready():
    return {"status": "ready"}


Instrumentator().instrument(app).expose(app)