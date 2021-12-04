import importlib.metadata

from fastapi import FastAPI

from src import PACKAGE_VERSION

app = FastAPI(
    title="Dumb service",
    description="Its all about upgrade version",
    version=PACKAGE_VERSION,
    docs_url="/swagger",
    redoc_url=None
)

@app.get("/")
def get_index():
    return {"Beep": "boop"}

@app.get("/version")
def get_version():
    package_version = importlib.metadata.version('auto-bump-version')
    return {"version": PACKAGE_VERSION}

