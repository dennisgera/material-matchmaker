import os

from fastapi import FastAPI
from app.meta import openapi_tags

app_version = os.getenv("VERSION", "0.0.0")

app = FastAPI(
    title="material-matchmaker",
    version=app_version,
    openapi_tags=openapi_tags,
    redirect_slashes=False,
)