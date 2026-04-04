from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from database import get_db, engine, Base
from models import Prayer
from schemas import PrayerOut
from seed import seed

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Siddur Guide API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/audio", StaticFiles(directory="/app/audio"), name="audio")


@app.on_event("startup")
def on_startup():
    seed()


@app.get("/api/prayers", response_model=list[PrayerOut])
def list_prayers(category: str | None = None, db: Session = Depends(get_db)):
    q = db.query(Prayer).order_by(Prayer.order_index)
    if category:
        q = q.filter(Prayer.category == category)
    return q.all()


@app.get("/api/prayers/{prayer_id}", response_model=PrayerOut)
def get_prayer(prayer_id: int, db: Session = Depends(get_db)):
    prayer = db.query(Prayer).filter(Prayer.id == prayer_id).first()
    if not prayer:
        raise HTTPException(status_code=404, detail="Prayer not found")
    return prayer


@app.get("/api/categories")
def list_categories(db: Session = Depends(get_db)):
    rows = db.query(Prayer.category).distinct().all()
    return [r[0] for r in rows]
