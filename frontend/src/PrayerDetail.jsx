import React, { useRef, useState } from 'react'

export default function PrayerDetail({ prayer, learned, onToggleLearned, onBack }) {
  const audioRef = useRef(null)
  const [playing, setPlaying] = useState(false)

  const toggleAudio = () => {
    if (!audioRef.current) return
    if (playing) {
      audioRef.current.pause()
    } else {
      audioRef.current.play()
    }
    setPlaying(!playing)
  }

  return (
    <div className="prayer-detail">
      <button className="back-btn" onClick={onBack}>← Back</button>

      <div className="detail-header">
        <div className="detail-icon">{prayer.icon || '✡'}</div>
        <h1 className="detail-name-he">{prayer.name_he}</h1>
        <h2 className="detail-name-en">{prayer.name_en}</h2>
        <span className="prayer-category">{prayer.category}</span>
      </div>

      <div className="detail-description">
        <p>{prayer.description}</p>
      </div>

      {prayer.audio_url && (
        <div className="audio-section">
          <button className="play-btn" onClick={toggleAudio}>
            {playing ? '⏸ Pause' : '▶ Play Audio'}
          </button>
          <audio
            ref={audioRef}
            src={prayer.audio_url}
            onEnded={() => setPlaying(false)}
          />
        </div>
      )}

      <button
        className={`learned-btn ${learned ? 'on' : ''}`}
        onClick={onToggleLearned}
      >
        {learned ? '✓ Marked as learned' : 'Mark as learned'}
      </button>

      <div className="text-section">
        <h3>Hebrew Text</h3>
        <p className="hebrew-text" dir="rtl">{prayer.text_hebrew}</p>
      </div>

      <div className="text-section">
        <h3>Transliteration (Cyrillic)</h3>
        <p className="transliteration">{prayer.transliteration}</p>
      </div>

      <div className="text-section">
        <h3>Translation (Russian)</h3>
        <p className="translation">{prayer.translation_ru}</p>
      </div>
    </div>
  )
}
