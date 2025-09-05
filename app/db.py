from sqlmodel import SQLModel, Session, create_engine
<<<<<<< HEAD
from app.models import Note, Transaction, User  # import all your models here
=======
from app.models import Note, Transaction  # import all your models here
>>>>>>> ea9a8b946a124ea57181e843c770834e13efafd1

DATABASE_URL = "sqlite:///./notetrade.db"
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session