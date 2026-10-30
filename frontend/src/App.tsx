import { useEffect, useState } from 'react'
import './App.css'

type Pokemon = {
  name: string
  level: number
  maxHp: number
  currentHp: number
  types: string[]
  status: string
}

function App() {

  const [party, setParty] = useState<Pokemon[]>([])

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
        })
        .catch(error => console.error(error))
    }

    fetchParty()

    const interval = setInterval(fetchParty, 2000)

    return () => clearInterval(interval)

  }, [])

  return (
    <div className="app">

      <h1>Pokémon Party Tracker</h1>

      {party.length === 0 && <p>No Pokémon data available.</p>}

      {party.map((pokemon, index) => (
        <div key={index} className="pokemon-card">

          <h2>{pokemon.name}</h2>

          <p>Level: {pokemon.level}</p>

          <p>Type: {pokemon.types.join(' / ')}</p>

          <p>HP: {pokemon.currentHp} / {pokemon.maxHp}</p>

          <progress
            value={pokemon.currentHp}
            max={pokemon.maxHp}
          />

          <p>Status: {pokemon.status}</p>

        </div>
      ))}

    </div>
  )
}

export default App