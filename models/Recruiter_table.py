from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey,JSON
from datetime import datetime 
from typing import List
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref,declarative_base,Mapped
from datetime import datetime
from database.connection import Base
from .Organization_table import Organization
class Recruiter(Base):
    __tablename__ = "recruiters"

    id = Column(String(255), primary_key=True)  # Unique user ID
    username = Column(String(255), unique=True, nullable=False)  # Unique username
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now())

    # One-to-Many relationship with ResumeApplicant (use backref for clarity)
    lists = relationship("ResumeRecruiter", backref="recruiter",lazy='dynamic')

    # Relationship with Organization (optional)
    organization_id = Column(Integer, ForeignKey('organizations.id'))
    # organization = relationship("Organization")
