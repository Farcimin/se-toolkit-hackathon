# Siddur Guide

An audio player with texts of core Jewish prayers in Hebrew, Cyrillic transliteration, translation, and audio of correct pronunciation.

---

## Project Idea

- **End-user:** Russian-speaking Jews and those interested in Judaism who want to learn how to properly recite Jewish prayers.
- **Problem:** Beginners struggle to correctly pronounce Hebrew prayers — there is no simple audio guide with transliterated texts in Cyrillic and explanations.
- **One sentence:** An audio guide for learning Jewish prayers with Hebrew text, Cyrillic transliteration, and correct pronunciation audio.
- **Core feature:** A catalog of essential prayers with text, transliteration, audio, and brief explanations.

---

## Implementation Plan

### Version 1 — Prayer Audio Guide

A catalog of essential Jewish prayers (Shema Yisrael, Amidah, blessings) with:

- Text in Hebrew
- Transliteration in Cyrillic
- Audio of correct pronunciation
- Brief description / explanation of each prayer

| Component | Technology | Purpose |
|-----------|------------|---------|
| Backend | FastAPI (Python) | REST API for prayers, audio files, search |
| Database | PostgreSQL | Stores prayers, texts, metadata, categories |
| Client | Web app (React) | Audio player with texts, prayer navigation |

### Version 2 — Enhancements + Deployment

Built on top of Version 1:

- **Prayer schedule** — display prayer times (Shacharit, Mincha, Maariv) based on user's city
- **User progress** — mark prayers as "learned"
- **Illustrations** — visual guides for prayer positions and actions
- Address TA feedback from V1 review
- Dockerize all services
- Deploy to university VM
