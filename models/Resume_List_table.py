from sqlalchemy import Column, String, Text, TypeDecorator, Integer, create_engine,MetaData,select,delete,ForeignKey
from email_validator import validate_email  # Optional for email validation
import json
from sqlalchemy.ext.mutable import MutableDict,MutableList
from sqlalchemy.types import ARRAY,JSON
from sqlalchemy.orm import declarative_base,relationship,Mapped
from typing import List
from database.connection import Base
class ResumeList(Base):
    __tablename__ = "resume_list"

    id = Column(Integer, primary_key=True,autoincrement=True)
    list_id = Column(Integer, ForeignKey("resumes_recruiter.id",ondelete='CASCADE'))
    list_name = Column(String(255))
    recruiter_id = Column(String(255))
    resume = Column(JSON)
    score = Column(Integer)