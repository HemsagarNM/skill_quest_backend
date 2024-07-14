from fastapi import APIRouter,UploadFile,File
from typing import Annotated 
from fastapi import Depends
from database.connection import get_dv,Base,engine
from .authentication import get_current_user
from sqlalchemy.orm import Session
from models.Applicant_table import Applicant
from models.Resumes_app_table import ResumeApplicant
from pydantic_models.oauth_access_model import AccessContorl
from backend.Parsing.pdftojson import get_resume_json
from backend.Parsing.resumejsonvalidator import ResumeValidator
from pydantic_models.ResumeLLM import ResumeLLM
from backend.ScoreGenerator import ScoreGenerator
import json
router = APIRouter(tags=['Applicant'])

Base.metadata.create_all(bind = engine)
@router.post("/uploadResume")
def upload_default_resumes(file: Annotated[UploadFile, File(description="file as UploadFile")],userinfo:AccessContorl = Depends(get_current_user), db : Session=Depends(get_dv)):
    u = db.query(Applicant).filter(Applicant.id==userinfo.uid).first()
    if u:
        resume_json = get_resume_json(file.file)
        resume_json = ResumeValidator(resume_json)._validate()
        resume_model = ResumeLLM(**resume_json)
        resume_app = ResumeApplicant(applicant_id = userinfo.uid, resume = resume_model.model_dump_json(),name = "default")
        u.resumes.append(resume_app)
        u.is_resume_uploaded = True
        db.add(resume_app)
        db.commit()
        resume_uploaded = db.refresh(resume_app)

        return resume_uploaded
    else:
        return "Unauthorised"
@router.post("/uploadResume/{resume_name}")
def upload_custom_resume(resume_name:str,file: Annotated[UploadFile, File(description="file as UploadFile")],userinfo:AccessContorl = Depends(get_current_user), db : Session=Depends(get_dv)):
    u = db.query(Applicant).filter(Applicant.id==userinfo.uid).first()
    if u:
        resume_json = get_resume_json(file.file)
        resume_json = ResumeValidator(resume_json)._validate()
        resume_model = ResumeLLM(**resume_json)
        resume_app = ResumeApplicant(applicant_id = userinfo.uid, resume = resume_model.model_dump_json(),name = resume_name)
        u.resumes.append(resume_app)
        db.add(resume_app)
        db.commit()
        resume_uploaded = db.refresh(resume_app)
        
        return resume_uploaded
        
    else:
        return "Unauthorised"

@router.get("/rankResume/{resume_name}")
def rank_custom_resume(resume_name:str,userinfo:AccessContorl = Depends(get_current_user), db : Session=Depends(get_dv)):
    u = db.query(Applicant).filter(Applicant.id==userinfo.uid).first()
    if u:
        for i in u.resumes:
            if i.name==resume_name:
                resume_json = json.loads(i.resume)
                resume_obj = ResumeLLM(**resume_json)
                score_gen = ScoreGenerator(resume_obj).get_score()
                return score_gen
    else:
        return "Unauthorised"
@router.post("/rankResume")
def rank_default_resume(userinfo:AccessContorl = Depends(get_current_user),db:Session = Depends(get_dv)):
    u = db.query(Applicant).filter(Applicant.id==userinfo.uid).first()
    if u:
        for i in u.resumes:
            if i.name=='default':
                resume_json = json.loads(i.resume)
                resume_obj = ResumeLLM(**resume_json)
                score_gen = ScoreGenerator(resume_obj).get_score()
                return score_gen
    else:
        return "Unauthorised"
    
@router.get("/resume/all")
def get_all_resumes(userinfo:AccessContorl = Depends(get_current_user),db:Session = Depends(get_dv)):
    u = db.query(Applicant).filter(Applicant.id==userinfo.uid).first()
    if u:
        resumes = {}
        for i in u.resumes:
                resume_json = json.loads(i.resume)
                resume_obj = ResumeLLM(**resume_json)
                resumes[i.name] = resume_obj
        return resumes
    else:
        return "Unauthorised"
@router.get("/resume/{resume_name}")
def get_custom_resume(resume_name:str,userinfo:AccessContorl = Depends(get_current_user),db:Session = Depends(get_dv)):
    u = db.query(Applicant).filter(Applicant.id==userinfo.uid).first()
    if u:
        for i in u.resumes:
            if i.name==resume_name:
                resume_json = json.loads(i.resume)
                resume_obj = ResumeLLM(**resume_json)
                return resume_obj
    else:
        return "Unauthorised"
    
@router.get("/resume")
def get_default_resume(userinfo:AccessContorl = Depends(get_current_user),db:Session = Depends(get_dv)):
    u = db.query(Applicant).filter(Applicant.id==userinfo.uid).first()
    if u:
        for i in u.resumes:
            if i.name=='default':
                resume_json = json.loads(i.resume)
                resume_obj = ResumeLLM(**resume_json)
                return resume_obj
    else:
        return "Unauthorised"
@router.delete("/resume/{resume_name}")
def delete_resume(resume_name:str,userinfo:AccessContorl = Depends(get_current_user),db:Session = Depends(get_dv)):
    u = db.query(Applicant).filter(Applicant.id==userinfo.uid).first()
    if u:

        if resume_name=='default':
            return "cannot delete default resume"
            
        else:
            for i in u.resumes:
                resume_json = json.loads(i.resume)
                resume_obj = ResumeLLM(**resume_json)
                db.query(ResumeApplicant).filter(ResumeApplicant.applicant_id ==userinfo.uid).filter(ResumeApplicant.name == resume_name) .delete()
                db.commit()
                print(resume_obj)
                return resume_obj
            