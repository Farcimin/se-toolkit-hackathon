from sqlalchemy import Column, Integer, String, Text
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
    order_index = Column(Integer, default=0)
