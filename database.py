from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL =  "postgresql+psycopg2://postgres:1234@localhost:5432/fastapiblog"



#  c:\Program Files\PostgreSQL\18\data\pg_hba.conf / trust
# services.msc = postgres / restart 

#  ALTER USER postgres PASSWORD '1234';  = parolni yaratasiz

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
# Only for SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
