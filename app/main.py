# app/main.py
from fastapi import FastAPI, UploadFile, File, Form, Depends, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select
from typing import List
import os

from app.models import Note, Transaction          # Transaction defined in app/models.py
from app.db import create_db_and_tables, get_session

app = FastAPI(title="NoteTrade")

# ───────── Static paths ─────────
templates = Jinja2Templates(directory="app/templates")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

# ───────── Startup ─────────
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# ───────── Pages ─────────
@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

@app.get("/upload", response_class=HTMLResponse)
def upload_form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@app.get("/notes", response_class=HTMLResponse)
def browse_notes(request: Request, session: Session = Depends(get_session)):
    notes: List[Note] = session.exec(select(Note).order_by(Note.id.desc())).all()
    return templates.TemplateResponse("index.html", {"request": request, "notes": notes})

@app.get("/transactions", response_class=HTMLResponse)
def transactions_page(request: Request, session: Session = Depends(get_session)):
    txs: List[Transaction] = session.exec(
        select(Transaction).order_by(Transaction.timestamp.desc())
    ).all()
    return templates.TemplateResponse(
        "transactions.html",
        {"request": request, "transactions": txs}
    )

# ───────── Actions ─────────
@app.post("/notes")
async def upload_note(
    title: str = Form(...),
    description: str = Form(""),
    file: UploadFile = File(...),
    session: Session = Depends(get_session),
):
    # store file
    file_path = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # DB record
    note = Note(title=title, description=description, file_path=file.filename)
    session.add(note)
    session.commit()

    return RedirectResponse("/notes", status_code=303)
