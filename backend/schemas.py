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
    order_index: int

    class Config:
        from_attributes = True
