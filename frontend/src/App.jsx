import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import MatchupPage from "./pages/MatchupPage";
import LeaderboardPage from "./pages/LeaderboardPage";

function App() {
  return (
    <Router>
      <nav>
        <Link to="/">Matchup</Link> | <Link to="/leaderboard">Leaderboard</Link>
      </nav>
      <Routes>
        <Route path="/" element={<MatchupPage />} />
        <Route path="/leaderboard" element={<LeaderboardPage />} />
      </Routes>
    </Router>
  );
}

export default App;
