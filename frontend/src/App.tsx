import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { LandingPage } from './pages/LandingPage';
import { ShelterMap } from './pages/ShelterMap';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/mapa" element={<ShelterMap />} />
      </Routes>
    </Router>
  );
}

export default App;