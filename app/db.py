from sqlmodel import SQLModel, Session, create_engine
from app.models import Note, Transaction

# Database URL (SQLite)
DATABASE_URL = "sqlite:///./notetrade.db"

# Create the engine
engine = create_engine(DATABASE_URL, echo=True)

#  Function to create tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

#  Function to get a DB session
def get_session():
    with Session(engine) as session:
        yield session