from fastapi import Depends, FastAPI
from api.routers import stocks
from .database import create_db_and_tables


app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(stocks.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
