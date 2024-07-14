from sqlalchemy import Column, String, ForeignKey,Integer,Boolean,Text, TypeDecorator,create_engine,MetaData,select,delete
from email_validator import validate_email  # Optional for email validation
import json
from sqlalchemy.ext.mutable import MutableDict,MutableList
from sqlalchemy.types import ARRAY,JSON
from sqlalchemy.orm import declarative_base,relationship,Mapped
from typing import List
from database.connection import Base
from models.Resume_List_table import ResumeList
class ResumeRecruiter(Base):
    __tablename__ = "resumes_recruiter"

    id = Column(Integer, primary_key=True,autoincrement=True)
    recruiter_id = Column(String(255), ForeignKey("recruiters.id" ,ondelete='CASCADE'))  # Foreign key to Applicant.id
    list_name = Column(String(255))
    resumelist = relationship("ResumeList", backref="ResumeRecruiter",lazy='dynamic')
    isExpereienced = Column(Boolean) 



if __name__ == "__main__":
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.mutable import MutableDict
    from pydantic import BaseModel,EmailStr
    from typing import Optional, List,Union
