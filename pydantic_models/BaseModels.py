from typing import Optional, List
from pydantic import BaseModel, EmailStr

class Address(BaseModel):
    city: str
    state: Optional[str]
    pinCode: Optional[str]
    country: Optional[str]


class Institution(BaseModel):
    name: str
    address: Optional[Address] = None or str


class EducationLevel(BaseModel):
    institution: Institution = None  
    board: Optional[str] = None   
    marks: str = None  
    duration: str
    start: str
    end: str


class Project(BaseModel):
    name: str
    description: str
    technologies: List[str]
    link: Optional[str] = None  


class Certification(BaseModel):
    name: str
    verificationLink: Optional[str]


class Experience(BaseModel):
    company: str   
    role: str = None  
    project: Optional[Project]
    duration: str = None  
    start: str = None  
    end: str = None  


class CodingPlatformLinks(BaseModel):
    leetCode: Optional[str]
    hackerRank: Optional[str]
    hackerEarth: Optional[str]
    codeChef: Optional[str]
    codeForces: Optional[str]
    gfg: Optional[str]


class PersonalInfo(BaseModel):
    name: str
    phoneNumber: str
    gitHub: str
    email: EmailStr
    dob: Optional[str] = None  
    address: Optional[Address] = None  


class OrganizationInfo(BaseModel):
    name: str
    id:int

class InstitutionInfo(BaseModel):
    name: str
    id:int

