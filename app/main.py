from app.db.mongo import db
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.shared.http import http_client
import httpx

app = FastAPI()

@app.on_event("startup")
async def startup():
    global http_client
    http_client = httpx.AsyncClient(timeout=10)

@app.on_event("shutdown")
async def shutdown():
    await http_client.aclose()
