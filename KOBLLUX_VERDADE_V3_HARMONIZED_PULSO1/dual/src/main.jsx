import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import ArchetypeInterface from './ArchetypeInterface.jsx'
import './index.css'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <ArchetypeInterface />
  </StrictMode>
)
