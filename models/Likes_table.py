from sqlalchemy import Column, String, Text, TypeDecorator, Integer, create_engine,MetaData,select,delete,ForeignKey
from email_validator import validate_email  # Optional for email validation
import json
from sqlalchemy.ext.mutable import MutableDict,MutableList
from sqlalchemy.types import ARRAY,JSON
from sqlalchemy.orm import declarative_base,relationship,Mapped
from typing import List
from database.connection import Base
from .Resumes_app_table import ResumeApplicant
from .Applicant_table import Applicant


class Like(Base):
    __tablename__ = "likes"
    id = Column(Integer,primary_key = True,autoincrement = True)
    resume_id = Column(Integer, ForeignKey("resumes_applicant.id"))
    applicant_id = Column(String(255), ForeignKey("applicants.id"))