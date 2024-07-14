from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from pydantic_models.BaseModels import PersonalInfo
import backend.ScoreGenerator as ScoreGenerator 
from backend.Parsing.ResumeParser import ResumeParser
from routes import ApplicantRouter
from routes import authentication,RecruiterRouter
from database.connection import engine,Base
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)
app=FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ApplicantRouter.router)
app.include_router(authentication.router)
app.include_router(RecruiterRouter.router)

