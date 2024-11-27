from sqlalchemy import create_engine
from sqlmodel import Session, SQLModel

import os
from dotenv import load_dotenv

load_dotenv()
POSTGRES_URL = os.getenv("POSTGRES_URL")

engine = create_engine(POSTGRES_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

        
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)