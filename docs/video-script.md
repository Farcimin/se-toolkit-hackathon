# Video Demo Script — Siddur Guide (≤ 2 minutes)

**Target length:** 90–110 seconds
**Recording tool:** macOS QuickTime (Cmd + Shift + 5 → Record Entire Screen + Microphone)
**URL to open in browser:** http://10.93.26.91:3000
**Before recording:** open the site, clear localStorage (DevTools → Application → Local Storage → Clear), reload so progress starts at 0/7.

---

## Scene 1 — Intro (0:00–0:12)

> "Hi, I'm Arslan. This is Siddur Guide — a web app that helps Russian-speaking beginners learn how to correctly read Jewish prayers in Hebrew, with audio, transliteration, and translation."

*[Show the Prayers tab — catalog with 7 prayers, progress bar, category filter.]*

---

## Scene 2 — Prayer catalog (0:12–0:28)

> "On the main screen, users see a catalog of core prayers — Shema Yisrael, Amidah, blessings, Shabbat liturgy. They can filter by category and see how many prayers they've already learned."

*[Click the "Daily" filter, then "All" again. Briefly hover over a few cards.]*

---

## Scene 3 — Prayer detail + audio (0:28–0:58)

> "Let's open Shema Yisrael — the most important prayer in Judaism. Each prayer shows three things side by side: the Hebrew text on the right, Cyrillic transliteration in the middle, and a Russian translation below. And the most important feature — an audio track with the correct Hebrew pronunciation."

*[Click the Shema Yisrael card. Wait for detail view to load. Click ▶ Play Audio — let it play for 5–7 seconds so the voice is clearly heard.]*

> "The audio is a Hebrew neural voice slowed down so beginners can follow along. Once a user feels confident with a prayer, they can mark it as learned."

*[Click "Mark as learned". Click ← Back.]*

---

## Scene 4 — Progress tracking (0:58–1:10)

> "Back on the catalog, the progress bar updates, and learned prayers get a green checkmark. Progress is saved on the backend, so it persists across browser sessions."

*[Show the catalog with the new "1/7 learned" state and the green check on Shema Yisrael.]*

---

## Scene 5 — Prayer times (1:10–1:38)

> "The second tab shows today's prayer times — Shacharit, Mincha, and Maariv — for the city the user picks. Everything is computed locally from latitude and longitude using the KosherJava zmanim algorithm, so no external API is needed."

*[Click the Times tab. Wait for it to load. Open the city dropdown, pick "Innopolis", and let the times update.]*

> "Here are today's times for Innopolis. The app supports ten cities including Jerusalem, Tel Aviv, Moscow, and New York."

*[Switch to Jerusalem to show it updates instantly.]*

---

## Scene 6 — Wrap-up (1:38–1:55)

> "Under the hood it's FastAPI, PostgreSQL, and React, all dockerized with a single docker compose up, and deployed on an Innopolis University VM. Code is on GitHub, MIT-licensed. Thanks for watching."

*[Optional: briefly show the GitHub page or the QR slide.]*

---

## Recording tips

- Speak slowly and clearly — you have plenty of time.
- Use Chrome or Safari in a clean window, zoom to ~110% for readability.
- Mute notifications before recording.
- Do one full take uninterrupted — if you stumble, start over.
- After recording, you can trim the start/end in QuickTime (Edit → Trim).
- Export as .mp4 at 1080p if possible.

## Words you might stumble on (quick reference)

- **Siddur** — SID-oor
- **Shema Yisrael** — shma yis-ra-EL
- **Shacharit** — sha-kha-REET
- **Mincha** — MIN-kha
- **Maariv** — ma-a-REEV
- **Amidah** — a-mee-DA
- **Zmanim** — zma-NEEM
- **KosherJava** — KO-sher JA-va
