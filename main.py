from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("work_in_progress.html", {"request": request})

@app.get("/index")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/events")
async def root():
    return {"message": "No events found!"}
