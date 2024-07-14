# Create an applicant
from .Resumes_app_table import ResumeApplicant
from .Applicant_table import Applicant
from .Resumes_recruiter_table import ResumeRecruiter
from .Recruiter_table import Recruiter

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from database.connection import Base 
from .Likes_table import Like
from setup import get_db_url
# applicant1 = Applicant(username="john_doe", email="john.doe12@example.com", password="hashed_password", is_student=True)

# # Create some resume data
# resume_data = {
#     "personalInfo":"erfeferf",
#     "education": "fferferferf",
#     # ... other resume sections
# }

# # Create a resume applicant record for the applicant
# resume_applicant1 = ResumeApplicant(applicant=applicant1, **resume_data)

# # Add the resume applicant to the applicant's resumes list (optional)
# applicant1.resumes.append(resume_applicant1)
# # applicant1.resumes.append(resume_applicant1)




# engine = create_engine(
#         SQLALCHEMY_DATABASE_URL
#     )

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def get_dv():
#     db=SessionLocal()
#     try:
#         return  db
#     except:
#             print('error')
# # Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)
# session = get_dv()

# # Save applicant and resume data to the database
# # session.add(applicant1)
# rows = session.query(ResumeApplicant).all()
# for i in rows:print(i.id)
# print("Hell World!")
# session.commit()
# session.close()



thumbs = Like(applicant_id = 1,resume_id = 1)
SQLALCHEMY_DATABASE_URL = get_db_url()

engine = create_engine(
        SQLALCHEMY_DATABASE_URL
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_dv():
    db=SessionLocal()
    try:
        return  db
    except:
            print('error') 
# Base.metadata.create_all(engine)
Base.metadata.drop_all(engine)
session = get_dv()
z = Recruiter(username="sdfsdfdsd", email="something@goodmal.cum",password="qwertrtits")
res_rec = ResumeRecruiter()
# z.resumes.append(res_rec)
# Save applicant and resume data to the database
# session.add(applicant1)
# session.add(thumbs)
# rows = session.query(Applicant).all()
# for row in rows:
#      print(row.id)

# res = session.query(Like).all()
# for row in res:
#      print(row.id,row.applicant_id,row.resume_id)
print("Hell World!")
session.commit()
session.close()