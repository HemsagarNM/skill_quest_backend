from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey,JSON
from datetime import datetime 
from typing import List
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref,declarative_base,Mapped
from datetime import datetime
from database.connection import Base
from .Institution_table import Institution
from .Organization_table import Organization
from .Resumes_app_table import ResumeApplicant
class Applicant(Base):
    __tablename__ = "applicants"

    id = Column(String(255), primary_key=True)  # Unique user ID
    username = Column(String(255), unique=True, nullable=False)  # Unique username
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    is_student = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    is_resume_uploaded = Column(Boolean, default=False)  # New column


    # One-to-Many relationship with ResumeApplicant (use backref for clarity)
    resumes = relationship("ResumeApplicant", backref="applicant")

    # Relationship with Institution (optional)
    institution_id = Column(Integer, ForeignKey('institutions.id'))
    # institution = relationship("Institution")

    # Relationship with Organization (optional)
    organization_id = Column(Integer, ForeignKey('organizations.id'))
    # organization = relationship("Organization")


# class ResumeApplicant(Base):
#     __tablename__ = "resumes_applicant"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     applicant_id = Column(Integer, ForeignKey("applicants.id"))  # Foreign key to Applicant.id

#     # Use separate columns for resume data or consider a dedicated model for complex resumes
#     personalInfo = Column(JSON)
#     education = Column(JSON)
#     projects = Column(JSON)
#     certifications = Column(JSON)
#     experience = Column(JSON)
#     codingPlatformLinks = Column(JSON)


if __name__=="__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from setup import get_db_url
    SQLALCHEMY_DATABASE_URL = get_db_url()

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(engine)
    # Base.metadata.drop_all(engine)
    def get_dv():
        db=SessionLocal()
        try:
            return  db
        except:
            print('error')
    # Base.metadata.create_all(engine)
    session = get_dv()
    # new_applicant = Applicant(
    #     username="john.doe",
    #     email="john.doe@example.com",
    #     password="hashed_password",  # Replace with a secure hashed password
    #     is_student=True,  # Change to False if student
    #     is_resume_uploaded=True,  # Set to True if resume uploaded
    #     institution_id=1,  # Set if applicant is a student (optional)
    #     organization_id=1,  # Set if applicant is not a student (optional)
    # )
    # new_r = ResumeApplicant(applicant_id = 1)

    # Add the new applicant to the session
    # session.add(new_applicant)
    # session.add(new_r)

    # Commit the changes to the database
    session.commit()
    # rows = session.query(ResumeApplicant).all()
    # for i in rows:print(i.applicant_id)
    # # Print a confirmation message
    # print(f"Applicant '{new_applicant.username}' created successfully!")

    # Close the session (optional, if not using the session elsewhere)
    session.close()