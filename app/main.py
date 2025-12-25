from fastapi import FastAPI
from app.routes import api, web
from app.db_connection import db

app = FastAPI()
# app.include_router(api.router, prefix="/api")
# app.include_router(web.router)

@app.get("/")
async def root():
    return {"message": "Hello world!"}
