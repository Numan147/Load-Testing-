import email
from http.client import HTTPException
from pyexpat import model
from turtle import st
from fastapi import FastAPI, Depends, status, HTTPException
import models, schemas, database
from database import engine, get_db
from sqlalchemy.orm import Session
from routers import detailsrouter
app = FastAPI()

models.Base.metadata.create_all(engine) 
app.include_router(detailsrouter.router)

