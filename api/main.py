from fastapi import FastAPI
from api.routers import stocks


app = FastAPI()
app.include_router(stocks.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
