from fastapi import APIRouter, Depends,status,HTTPException
from pyrebase import *
from setup import get_firebase_config
from setup import get_service_account
from fastapi.exceptions import HTTPException
import requests
from pydantic_models import Recruiter
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from database.connection import get_dv
from sqlalchemy.orm import Session
from models.Applicant_table import Applicant
from models.Recruiter_table import Recruiter
from pydantic_models.oauth_access_model import AccessContorl
from fastapi.responses import JSONResponse as jres
from pydantic_models import Applicant as applicant
import firebase_admin
from firebase_admin import credentials,auth
import os 



if not firebase_admin._apps:
    cred = credentials.Certificate(get_service_account()) 
    firebase_admin.initialize_app(cred)
firebaseConfig = get_firebase_config()
firebase = pyrebase.initialize_app(firebaseConfig)



router = APIRouter(tags=['accounts'])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@router.post("/signup")
async def create_account(user:applicant.ApplicantSignup,username:str,applicant:bool=True,db:Session = Depends(get_dv)):
    
    email = user.email
    password = user.password
    try:

        user = firebase.auth().create_user_with_email_and_password(email,password)
        
        if applicant:
            auth.set_custom_user_claims(user["localId"],{"access_level":1})
            new_applicant = Applicant(id=user['localId'],is_student=True,is_resume_uploaded=False,username=username,email=email,password=password)
            db.add(new_applicant)
            db.commit()
        else:
            auth.set_custom_user_claims(user["localId"],{"access_level":2})
            new_applicant = Recruiter(id=user['localId'],username=email,email=email,password=password)
            db.add(new_applicant)
            db.commit()


        firebase.auth().send_email_verification(user["idToken"])
        return "please verify email"
    
    except Exception as e:
        return HTTPException(status_code=400,detail="account already exists ")

    

@router.post("/login")
async def create_access_token(user:OAuth2PasswordRequestForm = Depends()):
    try:
        user = firebase.auth().sign_in_with_email_and_password(user.username,user.password)
        verify = firebase.auth().get_account_info(user["idToken"])['users'][0]
        
        if verify['emailVerified']:
             
                
            return applicant.Token (access_token=user["idToken"],token_type="bearer")
        
        return jres(content={"message":"verify your email"})
    except Exception as e :
        print(e)



@router.post("/reset_password")
def reset(user:applicant.ApplicantReset):
    try:
        firebase.auth().send_password_reset_email(user.email)
        return "password reset mail sent successfully"
    except:
        return "unknown error occured"



def verify_access_token(token:str,credentials_exception):
    try:
        
        user = auth.verify_id_token(id_token=token)
        # print(user)
        uid,access_level =  user['user_id'],user['access_level']
        return uid,access_level
    except:
        return credentials_exception
    
def get_current_user(token:str=Depends(oauth2_scheme)):
    credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"could not validate",headers={"WWW-Authenticate":"Bearer"})
    uid, access_level = verify_access_token(token,credentials_exception)
    userinfo = AccessContorl(uid=uid,level=access_level)
    return userinfo

def get_user_type(user_id:str=Depends(get_current_user)):
    pass

