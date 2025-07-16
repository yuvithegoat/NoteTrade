from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

# ───────── Note model ─────────
class Note(SQLModel, table=True):
    """
    A single note that a user can upload/trade.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True, max_length=200)
    description: str = Field(default="", max_length=600)
    file_path: str                     # e.g. "uploads/notes123.pdf"
    timestamp: datetime = Field(default_factory=datetime.utcnow)

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