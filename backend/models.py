from sqlalchemy import Column, Integer, String, Text, DateTime, UniqueConstraint
from sqlalchemy.sql import func
from database import Base


class Prayer(Base):
    __tablename__ = "prayers"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(100), nullable=False)
    name_en = Column(String(200), nullable=False)
    name_he = Column(String(200), nullable=False)
    text_hebrew = Column(Text, nullable=False)
    transliteration = Column(Text, nullable=False)
    translation_ru = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    audio_url = Column(String(500), nullable=True)
    icon = Column(String(10), nullable=True)
    order_index = Column(Integer, default=0)


class UserProgress(Base):
    __tablename__ = "user_progress"
    __table_args__ = (UniqueConstraint("user_id", "prayer_id", name="uq_user_prayer"),)

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(100), nullable=False, index=True)
    prayer_id = Column(Integer, nullable=False)
    learned_at = Column(DateTime(timezone=True), server_default=func.now())
