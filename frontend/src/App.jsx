import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import MatchupPage from "./pages/MatchupPage";
import LeaderboardPage from "./pages/LeaderboardPage";
import UserPage from "./pages/UserPage";

function App() {
  return (
    <Router>
      <nav>
        <Link to="/">Matchup</Link> | <Link to="/leaderboard">Leaderboard</Link> | <Link to="/users">Users</Link>
      </nav>
      <Routes>
        <Route path="/" element={<MatchupPage />} />
        <Route path="/leaderboard" element={<LeaderboardPage />} />
        <Route path="/users" element={<UserPage />} />
      </Routes>
    </Router>
  );
}

export default App;
