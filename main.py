from typing import Optional
from fastapi import FastAPI, Depends

from config.settings import Settings, get_settings

from routes import users

app = FastAPI()
app.include_router(users.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/settings")
async def read_settings(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }