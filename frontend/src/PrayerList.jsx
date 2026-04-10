import React from 'react'

export default function PrayerList({ prayers, learnedIds, onSelect }) {
  return (
    <div className="prayer-list">
      {prayers.map(p => {
        const isLearned = learnedIds && learnedIds.has(p.id)
        return (
          <div
            key={p.id}
            className={`prayer-card ${isLearned ? 'learned' : ''}`}
            onClick={() => onSelect(p)}
          >
            <div className="prayer-card-left">
              <span className="prayer-icon">{p.icon || '✡'}</span>
              <div className="prayer-card-header">
                <span className="prayer-name-he">{p.name_he}</span>
                <span className="prayer-name-en">{p.name_en}</span>
              </div>
            </div>
            <div className="prayer-card-right">
              {isLearned && <span className="check-badge">✓</span>}
              <span className="prayer-category">{p.category}</span>
            </div>
          </div>
        )
      })}
    </div>
  )
}
