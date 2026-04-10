from pydantic import BaseModel


class PrayerOut(BaseModel):
    id: int
    category: str
    name_en: str
    name_he: str
    text_hebrew: str
    transliteration: str
    translation_ru: str
    description: str
    audio_url: str | None
    icon: str | None
    order_index: int

    class Config:
        from_attributes = True


class ProgressIn(BaseModel):
    user_id: str
    prayer_id: int


class ProgressOut(BaseModel):
    prayer_id: int
    learned: bool


class ZmanimOut(BaseModel):
    city: str
    date: str
    shacharit: str | None
    mincha: str | None
    maariv: str | None
    sunrise: str | None
    sunset: str | None
