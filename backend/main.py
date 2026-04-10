from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from database import get_db, engine, Base
from models import Prayer, UserProgress
from schemas import PrayerOut, ProgressIn, ZmanimOut
from seed import seed
from zmanim import fetch_zmanim, list_cities

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Siddur Guide API", version="2.0")

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


@app.get("/api/health")
def health():
    return {"status": "ok", "version": "2.0"}


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


# --- V2: Progress tracking ---

@app.get("/api/progress/{user_id}")
def get_progress(user_id: str, db: Session = Depends(get_db)):
    rows = db.query(UserProgress.prayer_id).filter(UserProgress.user_id == user_id).all()
    return {"user_id": user_id, "learned_prayer_ids": [r[0] for r in rows]}


@app.post("/api/progress")
def mark_learned(body: ProgressIn, db: Session = Depends(get_db)):
    prayer = db.query(Prayer).filter(Prayer.id == body.prayer_id).first()
    if not prayer:
        raise HTTPException(status_code=404, detail="Prayer not found")
    try:
        entry = UserProgress(user_id=body.user_id, prayer_id=body.prayer_id)
        db.add(entry)
        db.commit()
    except IntegrityError:
        db.rollback()
    return {"status": "ok"}


@app.delete("/api/progress")
def unmark_learned(user_id: str, prayer_id: int, db: Session = Depends(get_db)):
    db.query(UserProgress).filter(
        UserProgress.user_id == user_id,
        UserProgress.prayer_id == prayer_id,
    ).delete()
    db.commit()
    return {"status": "ok"}


# --- V2: Prayer times (Zmanim) ---

@app.get("/api/zmanim", response_model=ZmanimOut)
def get_zmanim(city: str = "Jerusalem", date: str | None = None):
    try:
        data = fetch_zmanim(city, date)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Zmanim error: {e}")
    return data


@app.get("/api/cities")
def get_cities():
    return list_cities()
