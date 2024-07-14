# from .BaseModels import PersonalInfo,EducationLevel,Project,Certification,Experience,CodingPlatformLinks
from pydantic import BaseModel,EmailStr
from typing import Optional, List,Union





class AddressLLM(BaseModel):
    city: Optional[str] = None
    state: Optional[str] = None
    pinCode: Optional[str] = None
    country: Optional[str] = None


class InstitutionLLM(BaseModel):
    name: Optional[str] = None
    address: Optional[AddressLLM] = None


class EducationLevelLLM(BaseModel):
    institution: Optional[InstitutionLLM] = None 
    board: Optional[str] = None  
    marks: Optional[str] = None 
    duration: Optional[str] = None
    start: Optional[str] = None
    end: Optional[str] = None


class ProjectLLM(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    technologies: Optional[List[str]] = None
    link: Optional[str] = None

class CertificationLLM(BaseModel):
    name: Optional[str] = None
    verificationLink: Optional[str] = None


class ExperienceLLM(BaseModel):
   company: Optional[str] = None   
   role: Optional[str] = None  
   project: Optional[ProjectLLM] = None
   duration: Optional[str] = None   
   start: Optional[str] = None   
   end: Optional[str] = None  


class CodingPlatformLinksLLM(BaseModel):
    leetCode: Optional[str] = None
    hackerRank: Optional[str] = None
    hackerEarth: Optional[str] = None
    codeChef: Optional[str] = None
    codeForces: Optional[str] = None
    gfg: Optional[str] = None


class PersonalInfoLLM(BaseModel):
    name: Optional[str] = None
    phoneNumber: Optional[str] = None
    gitHub: Optional[str] = None
    email: Optional[EmailStr] = None
    dob: Optional[str] = None  
    address: Optional[AddressLLM] = None  


class OrganizationInfo(BaseModel):
    name: Optional[str] = None
    id:Optional[str] = None

class InstitutionInfo(BaseModel):
    name: Optional[str] = None
    id:Optional[int] = None

class ResumeLLM(BaseModel):
    personalInfo: Optional[PersonalInfoLLM] = None
    education: Optional[dict[str, EducationLevelLLM]] = [None,None]
    projects: Optional[List[ProjectLLM]] = None 
    certifications: Optional[List[CertificationLLM]] = None
    experience: Optional[List[ExperienceLLM]] = None
    codingPlatformLinks: Optional[CodingPlatformLinksLLM] = None






if __name__=="__main__":


    jsum=resume_data



    from .sampleResume import resume_data
    try:
        resume = ResumeLLM(**resume_data)
        print(resume)
        print(resume.projects[0].link)
    except Exception as e:
        print(e)
