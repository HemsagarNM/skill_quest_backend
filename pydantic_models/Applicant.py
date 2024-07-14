from .BaseModels import PersonalInfo,OrganizationInfo,InstitutionInfo
from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime
class ApplicantCreate(BaseModel):
    username:str
    created_at:datetime
    current_organization: Optional[OrganizationInfo] = None
    current_institution: Optional[InstitutionInfo] = None
    isStudent:bool
    resumeScore:float
    email:EmailStr
    id:int


class ApplicantSignup(BaseModel):
    email:EmailStr
    password:str

class ApplicantResponse(BaseModel):
    email:EmailStr
    created_at:str

class ApplicantLogin(BaseModel):
    username:EmailStr
    password:str

class ApplicantReset(BaseModel):
    email:EmailStr

class Token(BaseModel):
    access_token:str
    token_type:str



if __name__=="__main__":
    from sampleResume import resume_data
    try:
        resume = ApplicantCreate(resume=resume_data,username="sdfdsf",created_at="sdfdfdf")
        print(resume)
        print(resume.projects[0].link)
    except Exception as e:
        print(e)
