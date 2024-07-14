from .BaseModels import PersonalInfo,OrganizationInfo,InstitutionInfo
from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime

class AccessContorl(BaseModel):
    uid:str
    level:int


class Token(BaseModel):
    access_token:str
    token_type:str