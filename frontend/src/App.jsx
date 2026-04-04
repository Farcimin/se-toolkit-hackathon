import React, { useState, useEffect } from 'react'
import PrayerList from './PrayerList.jsx'
import PrayerDetail from './PrayerDetail.jsx'
import './styles.css'

export default function App() {
  const [prayers, setPrayers] = useState([])
  const [categories, setCategories] = useState([])
  const [selectedCategory, setSelectedCategory] = useState(null)
  const [selectedPrayer, setSelectedPrayer] = useState(null)

  useEffect(() => {
    fetch('/api/categories').then(r => r.json()).then(setCategories)
    fetch('/api/prayers').then(r => r.json()).then(setPrayers)
  }, [])

  const filtered = selectedCategory
    ? prayers.filter(p => p.category === selectedCategory)
    : prayers

  if (selectedPrayer) {
    return (
      <div className="app">
        <PrayerDetail prayer={selectedPrayer} onBack={() => setSelectedPrayer(null)} />
      </div>
    )
  }

  return (
    <div className="app">
      <header className="header">
        <h1>✡ Siddur Guide</h1>
        <p className="subtitle">Learn Jewish prayers with audio and transliteration</p>
      </header>

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

      <PrayerList prayers={filtered} onSelect={setSelectedPrayer} />
    </div>
  )
}
