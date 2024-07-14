from fastapi import APIRouter,File, UploadFile
from fastapi import Depends
from database.connection import get_dv,Base,engine
from .authentication import get_current_user
from sqlalchemy.orm import Session
from models.Applicant_table import Applicant
from models.Resumes_app_table import ResumeApplicant
from models.Recruiter_table import Recruiter
from models.Resume_List_table import ResumeList
# from models.
from pydantic_models.ResumeLLM import ResumeLLM
from models.Resumes_recruiter_table import ResumeRecruiter
from pydantic_models.oauth_access_model import AccessContorl
from typing import Annotated
from backend.Parsing.pdftojson import get_resume_json
from backend.Parsing.resumejsonvalidator import ResumeValidator
from backend.ScoreGenerator import ScoreGenerator
from sqlalchemy import delete
import json
router = APIRouter(tags=['Recruiter'])

Base.metadata.create_all(bind = engine)
@router.get("/list/{list_name}/rankresumes")
def get_resumes(list_name:str,userinfo:AccessContorl = Depends(get_current_user), db : Session=Depends(get_dv)):
    if userinfo.level >= 2:

        u = db.query(Recruiter).filter(Recruiter.id==userinfo.uid).first()
        statistics = []
        for i in u.lists:
            for j in i.resumelist:
                if j.list_name == list_name and userinfo.uid == j.recruiter_id:
                    resume = json.loads(j.resume)
                    resume_py_obj = ResumeLLM(**resume)
                    stats = ScoreGenerator(resume_py_obj).get_score()
                    stats.update({'resume_id':j.id})
                    statistics.append(stats)

        return statistics
    else:
        return 'Unauthorised error'

@router.get("/list")
def get_list(userinfo:AccessContorl = Depends(get_current_user), db : Session=Depends(get_dv)):
    if userinfo.level >= 2:
        u = db.query(Recruiter).filter(Recruiter.id==userinfo.uid).first()
        lists_list = []
        for i in u.lists:
            if i.recruiter_id == userinfo.uid:
                lists_list.append(i.list_name)
        return lists_list

    else:
        return "Unauthorised error"
@router.delete("/list/{list_name}/{resume_id}")
def delete_resume(list_name:str,resume_id:int,userinfo:AccessContorl = Depends(get_current_user), db : Session=Depends(get_dv)):
    if userinfo.level >= 2:
        u = db.query(Recruiter).filter(Recruiter.id==userinfo.uid).first()
        for i in u.lists:
            for j in i.resumelist:
                if j.list_name == list_name and userinfo.uid == j.recruiter_id: 
                    res = db.query(ResumeList).filter(ResumeList.recruiter_id==userinfo.uid).filter(ResumeList.list_name==list_name).filter(ResumeList.id==resume_id).delete()
                    db.commit()
        return True
@router.get("/list/{list_name}/{resume_id}")
def get_resume(list_name:str,resume_id:int,userinfo:AccessContorl = Depends(get_current_user), db : Session=Depends(get_dv)):
    if userinfo.level >= 2:
        u = db.query(Recruiter).filter(Recruiter.id==userinfo.uid).first()
        for i in u.lists:
            for j in i.resumelist:
                if j.list_name == list_name and userinfo.uid == j.recruiter_id: 
                    res = db.query(ResumeList).filter(ResumeList.recruiter_id==userinfo.uid).filter(ResumeList.list_name==list_name).filter(ResumeList.id==resume_id).first()
                    resume_json = json.loads(res.resume)
                    return resume_json
        return True
@router.get("/list/{resume_id}")
def get_resume(resume_id:int,userinfo:AccessContorl = Depends(get_current_user), db : Session=Depends(get_dv)):
    if userinfo.level >= 2:
        u = db.query(ResumeList).filter(Recruiter.id==userinfo.uid)
        for i in u:
                if i.id==resume_id:
                    resume_json = json.loads(i.resume)
                    return resume_json
        return False
@router.delete("/list/{list_name}")
def delete_list(list_name:str,userinfo:AccessContorl = Depends(get_current_user), db : Session=Depends(get_dv)):
    if userinfo.level >= 2:
        u = db.query(Recruiter).filter(Recruiter.id==userinfo.uid).first()
        for i in u.lists:
            if i.list_name==list_name:
                db.query(ResumeRecruiter).filter(ResumeRecruiter.recruiter_id==userinfo.uid).filter(ResumeRecruiter.list_name==list_name).delete()
                db.commit()
        return True


@router.post("/list/uploadresumes/{list_name}")
def get_uploaded_resumes(list_name:str,files: Annotated[list[UploadFile], File(description="Multiple files as UploadFile")],userinfo:AccessContorl = Depends(get_current_user), db : Session=Depends(get_dv)):

    if userinfo.level >= 2:
        count = 0
        list_obj = db.query(ResumeRecruiter).filter(ResumeRecruiter.recruiter_id==userinfo.uid).filter(ResumeRecruiter.list_name == list_name).first()
        if not list_obj:
            list_obj = ResumeRecruiter(recruiter_id = userinfo.uid,list_name = list_name)
            for file in files:
                resume_json = get_resume_json(file.file)
                resume_json = ResumeValidator(resume_json)._validate()
                resume_json = ResumeLLM(**resume_json)
                resume_obj = ResumeList(list_name = list_name,recruiter_id = userinfo.uid,resume = resume_json.model_dump_json())
                list_obj.resumelist.append(resume_obj)
                count += 1
            db.add(list_obj)
            db.commit()
        else:
            for file in files:
                pass

                resume_json = get_resume_json(file.file)
                resume_json = ResumeValidator(resume_json)._validate()
                resume_json = ResumeLLM(**resume_json)
                resume_obj = ResumeList(list_name = list_name,recruiter_id = userinfo.uid,resume = resume_json.model_dump_json())
                list_obj.resumelist.append(resume_obj)
                count += 1
            # db.add(list_obj)
            db.commit()
        return count
        
    else: 
        return 'Unauthorised error'


