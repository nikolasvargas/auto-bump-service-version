import importlib.metadata

from datetime import datetime

from fastapi import FastAPI

from autobump import PACKAGE_VERSION, API_VERSION

app = FastAPI(
    title="Dumb service",
    description="Its all about upgrade version",
    version=API_VERSION,
    docs_url="/swagger",
    redoc_url=None
)

@app.get("/")
def get_index():
    return {"Beep": "boop"}


@app.get("/health")
def get_health():
    return {
        "ok": True,
        "datetime": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    }


@app.get("/versions")
def get_version():
    return {
        "api_version": API_VERSION,
        "package_name": "auto-bump-version",
        "package_version": PACKAGE_VERSION
    }
