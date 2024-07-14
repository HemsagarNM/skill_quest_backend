from pydantic_models.BaseModels import PersonalInfo,OrganizationInfo
from pydantic import EmailStr,BaseModel
from typing import Optional
from datetime import datetime 
class RecruiterCreate(BaseModel):
    username:str
    personalInfo:Optional[PersonalInfo] = None
    organization:OrganizationInfo
    organization_mail:EmailStr

class RecruiterResponse(BaseModel):
    email:EmailStr
    create_at:datetime

class RecruiterSignup(BaseModel):
    email:EmailStr
    password:str


class RecruiterLogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:Optional[int]

    


