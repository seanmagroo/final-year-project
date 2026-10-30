import { useEffect, useState } from 'react'
import './App.css'

type Pokemon = {
  species_Id: number
  name: string
  level: number
  maxHp: number
  currentHp: number
  types: string[]
  status: string | null
  baseStats: Record<string, number>
  blockA: Record<string, unknown>
  blockB: Record<string, unknown>
}

// Make dictionary keys more readable
function formatLabel(key: string): string {
  return key
    .replace(/_/g, ' ')
    .replace(/([a-z])([A-Z])/g, '$1 $2')
    .replace(/([a-zA-Z])(\d)/g, '$1 $2')
    .replace(/\b\w/g, letter => letter.toUpperCase())
}

// Convert nested dictionary fields into displayable rows
function getRows(
  data: Record<string, unknown>,
  prefix = ''
): { label: string; value: string }[] {

  return Object.entries(data).flatMap(([key, value]) => {
    const label = prefix
      ? `${prefix} / ${formatLabel(key)}`
      : formatLabel(key)

    if (value !== null && typeof value === 'object' && !Array.isArray(value)) {
      return getRows(value as Record<string, unknown>, label)
    }

    const displayValue = Array.isArray(value)
      ? value.map(item =>
          typeof item === 'object' ? JSON.stringify(item) : String(item)
        ).join(', ')
      : String(value ?? '—')

    return [{ label, value: displayValue }]
  })
}

// Reusable component for displaying Pokémon attributes
function DataSection({
  title,
  data
}: {
  title: string
  data: Record<string, unknown>
}) {
  return (
    <section className="data-section">
      <h3>{title}</h3>

      <div className="stats-grid">
        {getRows(data).map((row, index) => (
          <div className="stat" key={index}>
            <span className="stat-label">{row.label}</span>
            <span className="stat-value">{row.value}</span>
          </div>
        ))}
      </div>
    </section>
  )
}

function App() {

  const [party, setParty] = useState<Pokemon[]>([])
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {

    const fetchParty = () => {
      fetch('/party')
        .then(response => {
          if (!response.ok) {
            throw new Error('Failed to fetch Pokémon data')
          }
          return response.json()
        })
        .then((data: Pokemon[]) => {
          setParty(data)
          setError(null)
        })
        .catch(error => {
          console.error(error)
          setError('Unable to retrieve the latest Pokémon data.')
        })
    }

    fetchParty()

    const interval = setInterval(fetchParty, 2000)

    return () => clearInterval(interval)

  }, [])

  return (
    <div className="app">

      <h1>Pokémon Party Tracker</h1>

      {error && <p className="error">{error}</p>}

      {party.length === 0 && <p>No Pokémon data available.</p>}

      <div className="party-grid">
        {party.map((pokemon, index) => (

          <div key={index} className="pokemon-card">

            <div className="pokemon-header">

              <img
                className="pokemon-sprite"
                src={`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-iv/platinum/${pokemon.species_Id}.png`}
                alt={pokemon.name}
                width={96}
                height={96}
              />

              <div>
                <h2>{pokemon.name}</h2>
                <p>Level {pokemon.level}</p>
                <p>{pokemon.types.join(' / ')}</p>
              </div>

            </div>

            <div className="hp-section">
              <p>HP: {pokemon.currentHp} / {pokemon.maxHp}</p>

              <progress
                value={pokemon.currentHp}
                max={pokemon.maxHp}
              />

              <p>Status: {pokemon.status || 'Healthy'}</p>
            </div>

            <DataSection
              title="Base Stats"
              data={pokemon.baseStats}
            />

            <DataSection
              title="Training, Ability & Other Attributes"
              data={pokemon.blockA}
            />

            <DataSection
              title="Moves, PP & IVs"
              data={pokemon.blockB}
            />

          </div>

        ))}
      </div>

    </div>
  )
}

export default App