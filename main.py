from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router as list_router
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import ListModel, ListUpdateModel

config = dotenv_values(".env")

app = FastAPI()
router = APIRouter()

app.include_router(list_router, tags=["list"], prefix="/list")

#Start the connection with MongoDB database once the application starts
@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGODB_CONNECTION_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")
#Close the connection
@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()



