from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from database.connection import Base

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(255), nullable=False,unique=True)
    location = Column(String(255))


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from setup import get_db_url
    new_organization = Organization(
        name="Awesome Organization",
        location="Anytown, USA",
    )


    SQLALCHEMY_DATABASE_URL = get_db_url()
    
    engine = create_engine(
    SQLALCHEMY_DATABASE_URL
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(engine)
    import sqlalchemy

    def get_dv():
        db=SessionLocal()
        try:
            return db
        except:
            print('error')

    Base.metadata.create_all(engine)

    session = get_dv()
        # Add the organization to the session (optional, if creating applicants)
    session.add(new_organization)

        # Commit the changes to the database (optional, if creating applicants)
    session.commit()

    print(f"Organization '{new_organization.name}' created successfully!")

        # Close the session (optional, if not using the session elsewhere)
    session.close()