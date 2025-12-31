from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.api import api, web
from app.db.mongo import db
from app.advisories.repository import get_all_countries

app = FastAPI()
app.include_router(api.router)
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
async def root():
    countries = await get_all_countries()
    return templates.TemplateResponse("index.html", {"request": Request, "countries": countries})   
