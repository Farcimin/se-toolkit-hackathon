import React from 'react'

export default function PrayerList({ prayers, onSelect }) {
  return (
    <div className="prayer-list">
      {prayers.map(p => (
        <div key={p.id} className="prayer-card" onClick={() => onSelect(p)}>
          <div className="prayer-card-header">
            <span className="prayer-name-he">{p.name_he}</span>
            <span className="prayer-name-en">{p.name_en}</span>
          </div>
          <span className="prayer-category">{p.category}</span>
        </div>
      ))}
    </div>
  )
}
