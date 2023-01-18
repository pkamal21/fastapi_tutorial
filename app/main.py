from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import models, config
from app.database import engine
from app.routers import auth, team, stock, user

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def root():
    return {"message": "Welcome to finance_11 API. \nIf you're a finance_11 employee, please check /docs to use the API, else you should leave or talk to our customer care.."}

app.include_router(auth.router)
app.include_router(stock.router)
app.include_router(team.router)
app.include_router(user.router)
