import React, { useState, useEffect } from "react";
import axios from "axios";

const LeaderboardPage = () => {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    axios.get(`${import.meta.env.VITE_BACKEND_URL}/leaderboard`)
      .then((res) => setLeaderboard(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div>
      <h2>Leaderboard</h2>
      <ul>
        {leaderboard.map((user, index) => (
          <li key={user.id}>
            {index + 1}. {user.name} - Elo: {user.elo}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default LeaderboardPage;
