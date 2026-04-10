import React, { useState, useEffect } from 'react'
import PrayerList from './PrayerList.jsx'
import PrayerDetail from './PrayerDetail.jsx'
import Schedule from './Schedule.jsx'
import './styles.css'

function getUserId() {
  let id = localStorage.getItem('siddur_user_id')
  if (!id) {
    id = 'u_' + Math.random().toString(36).slice(2, 12)
    localStorage.setItem('siddur_user_id', id)
  }
  return id
}

export default function App() {
  const [prayers, setPrayers] = useState([])
  const [categories, setCategories] = useState([])
  const [selectedCategory, setSelectedCategory] = useState(null)
  const [selectedPrayer, setSelectedPrayer] = useState(null)
  const [learnedIds, setLearnedIds] = useState(new Set())
  const [tab, setTab] = useState('prayers') // 'prayers' | 'schedule'
  const userId = getUserId()

  useEffect(() => {
    fetch('/api/categories').then(r => r.json()).then(setCategories)
    fetch('/api/prayers').then(r => r.json()).then(setPrayers)
    fetch(`/api/progress/${userId}`)
      .then(r => r.json())
      .then(d => setLearnedIds(new Set(d.learned_prayer_ids || [])))
  }, [])

  const toggleLearned = async (prayerId) => {
    const isLearned = learnedIds.has(prayerId)
    if (isLearned) {
      await fetch(`/api/progress?user_id=${userId}&prayer_id=${prayerId}`, { method: 'DELETE' })
      const next = new Set(learnedIds)
      next.delete(prayerId)
      setLearnedIds(next)
    } else {
      await fetch('/api/progress', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: userId, prayer_id: prayerId }),
      })
      setLearnedIds(new Set([...learnedIds, prayerId]))
    }
  }

  const filtered = selectedCategory
    ? prayers.filter(p => p.category === selectedCategory)
    : prayers

  if (selectedPrayer) {
    return (
      <div className="app">
        <PrayerDetail
          prayer={selectedPrayer}
          learned={learnedIds.has(selectedPrayer.id)}
          onToggleLearned={() => toggleLearned(selectedPrayer.id)}
          onBack={() => setSelectedPrayer(null)}
        />
      </div>
    )
  }

  const progressPct = prayers.length
    ? Math.round((learnedIds.size / prayers.length) * 100)
    : 0

  return (
    <div className="app">
      <header className="header">
        <h1>✡ Siddur Guide</h1>
        <p className="subtitle">Learn Jewish prayers with audio and transliteration</p>
      </header>

      <div className="tabs">
        <button
          className={`tab-btn ${tab === 'prayers' ? 'active' : ''}`}
          onClick={() => setTab('prayers')}
        >
          📖 Prayers
        </button>
        <button
          className={`tab-btn ${tab === 'schedule' ? 'active' : ''}`}
          onClick={() => setTab('schedule')}
        >
          🕒 Times
        </button>
      </div>

      {tab === 'prayers' && (
        <>
          <div className="progress-bar-wrap">
            <div className="progress-label">
              Progress: {learnedIds.size} / {prayers.length} learned ({progressPct}%)
            </div>
            <div className="progress-bar">
              <div className="progress-fill" style={{ width: `${progressPct}%` }} />
            </div>
          </div>

          <div className="categories">
            <button
              className={`cat-btn ${!selectedCategory ? 'active' : ''}`}
              onClick={() => setSelectedCategory(null)}
            >
              All
            </button>
            {categories.map(c => (
              <button
                key={c}
                className={`cat-btn ${selectedCategory === c ? 'active' : ''}`}
                onClick={() => setSelectedCategory(c)}
              >
                {c}
              </button>
            ))}
          </div>

          <PrayerList
            prayers={filtered}
            learnedIds={learnedIds}
            onSelect={setSelectedPrayer}
          />
        </>
      )}

      {tab === 'schedule' && <Schedule />}
    </div>
  )
}
