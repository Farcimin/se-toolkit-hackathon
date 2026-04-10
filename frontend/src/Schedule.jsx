import React, { useEffect, useState } from 'react'

export default function Schedule() {
  const [cities, setCities] = useState([])
  const [city, setCity] = useState(localStorage.getItem('siddur_city') || 'Jerusalem')
  const [zmanim, setZmanim] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetch('/api/cities').then(r => r.json()).then(setCities)
  }, [])

  useEffect(() => {
    setLoading(true)
    setError(null)
    fetch(`/api/zmanim?city=${encodeURIComponent(city)}`)
      .then(r => {
        if (!r.ok) throw new Error('Failed to load prayer times')
        return r.json()
      })
      .then(d => {
        setZmanim(d)
        setLoading(false)
        localStorage.setItem('siddur_city', city)
      })
      .catch(e => {
        setError(e.message)
        setLoading(false)
      })
  }, [city])

  return (
    <div className="schedule">
      <div className="schedule-header">
        <h2>Today's Prayer Times</h2>
        <select
          className="city-select"
          value={city}
          onChange={e => setCity(e.target.value)}
        >
          {cities.map(c => (
            <option key={c} value={c}>{c}</option>
          ))}
        </select>
      </div>

      {loading && <div className="loading">Loading...</div>}
      {error && <div className="error">{error}</div>}

      {zmanim && !loading && (
        <div className="zmanim-grid">
          <div className="zmanim-card">
            <div className="zmanim-icon">🌅</div>
            <div className="zmanim-label">Sunrise</div>
            <div className="zmanim-time">{zmanim.sunrise || '—'}</div>
          </div>
          <div className="zmanim-card primary">
            <div className="zmanim-icon">☀️</div>
            <div className="zmanim-label">Shacharit</div>
            <div className="zmanim-time">{zmanim.shacharit || '—'}</div>
            <div className="zmanim-hint">Morning prayer</div>
          </div>
          <div className="zmanim-card primary">
            <div className="zmanim-icon">🌤️</div>
            <div className="zmanim-label">Mincha</div>
            <div className="zmanim-time">{zmanim.mincha || '—'}</div>
            <div className="zmanim-hint">Afternoon prayer</div>
          </div>
          <div className="zmanim-card primary">
            <div className="zmanim-icon">🌙</div>
            <div className="zmanim-label">Maariv</div>
            <div className="zmanim-time">{zmanim.maariv || '—'}</div>
            <div className="zmanim-hint">Evening prayer</div>
          </div>
          <div className="zmanim-card">
            <div className="zmanim-icon">🌇</div>
            <div className="zmanim-label">Sunset</div>
            <div className="zmanim-time">{zmanim.sunset || '—'}</div>
          </div>
        </div>
      )}

      <p className="schedule-footer">
        Times provided by <a href="https://www.hebcal.com/" target="_blank" rel="noreferrer">HebCal</a>
      </p>
    </div>
  )
}
