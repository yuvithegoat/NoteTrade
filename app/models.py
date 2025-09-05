from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

# ───────── Transaction model ─────────
class Transaction(SQLModel, table=True):
    """
    Records each sale / purchase of a note.
    """
    id: Optional[int] = Field(default=None, primary_key=True)

    note_id: int                       # FK → Note.id
    buyer: str                         # username / identifier of buyer
    price: float                       # price paid
    timestamp: datetime = Field(default_factory=datetime.utcnow)
<<<<<<< HEAD
=======
from typing import Optional
from sqlmodel import SQLModel, Field

>>>>>>> ea9a8b946a124ea57181e843c770834e13efafd1

class Note(SQLModel, table=True):
    __table_args__ = {"extend_existing": True}

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    subject: str
    category: str
    price: float
<<<<<<< HEAD
    file_path: str

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
=======
    file_path: str
>>>>>>> ea9a8b946a124ea57181e843c770834e13efafd1
