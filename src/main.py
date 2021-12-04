import importlib.metadata
from fastapi import FastAPI

app = FastAPI(
    title="Dumb service",
    description="Its all about upgrade version",
    version="0.0.1",
    docs_url="/swagger",
    redoc_url=None
)

@app.get("/")
def get_index():
    return {"Beep": "boop"}

@app.get("/version")
def get_version():
    package_version = importlib.metadata.version('auto-bump-version')
    return {"version": package_version}

