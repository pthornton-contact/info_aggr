import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import FeedsDashboard from './pages/FeedsDashboard';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <header className="bg-blue-500 text-white p-4">
          <h1 className="text-xl">Feeds Curation Dashboard</h1>
          <nav>
            <ul className="flex space-x-4">
              <li>
                <Link to="/">Feeds</Link>
              </li>
              <li>
                <Link to="/api/users">Users</Link>
              </li>
            </ul>
          </nav>
        </header>
        <main className="p-4">
          <Routes>
            <Route path="/" element={<FeedsDashboard />} />
            {/* Add more routes for other pages like UsersDashboard */}
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;