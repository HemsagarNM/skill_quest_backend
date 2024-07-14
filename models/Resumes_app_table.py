from sqlalchemy import Column, String, Text, TypeDecorator, Integer, create_engine,MetaData,select,delete,ForeignKey
from email_validator import validate_email  # Optional for email validation
import json
from sqlalchemy.ext.mutable import MutableDict,MutableList
from sqlalchemy.types import ARRAY,JSON
from sqlalchemy.orm import declarative_base,relationship,Mapped
from typing import List
from database.connection import Base
class ResumeApplicant(Base):
    __tablename__ = "resumes_applicant"

    id = Column(Integer, primary_key=True, autoincrement=True)
    applicant_id = Column(String, ForeignKey("applicants.id"))  # Foreign key to Applicant.id

    # Use separate columns for resume data or consider a dedicated model for complex resumes
    name = Column(String)
    resume = Column(JSON)
    score = Column(Integer)

if __name__ == "__main__":
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.mutable import MutableDict
    from pydantic import BaseModel,EmailStr
    from typing import Optional, List,Union