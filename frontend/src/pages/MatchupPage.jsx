import React, { useState, useEffect } from "react";
import axios from "axios";

const MatchupPage = () => {
  const [profiles, setProfiles] = useState(null);

  useEffect(() => {
    axios.get(`${import.meta.env.VITE_BACKEND_URL}/api/matchups/matchup`)
      .then((res) => setProfiles(res.data))
      .catch((err) => console.error(err));
  }, []);

  const handleVote = (winnerId, loserId) => {
    axios.post(`${import.meta.env.VITE_BACKEND_URL}/api/matchups/submit`, {
      winner_id: winnerId,
      loser_id: loserId,
    }).then(() => window.location.reload());
    console.log("Winner ID:", winnerId);
    console.log("Loser ID:", loserId);
  };

  if (!profiles) return <p>Loading...</p>;

  return (
    <div>
      <h2>Which LinkedIn profile is better?</h2>
      <div>
        <button onClick={() => handleVote(profiles['user1'], profiles['user2'])}>
          {profiles['user1'].name}
        </button>
        <span> VS </span>
        <button onClick={() => handleVote(profiles['user2'], profiles['user1'])}>
          {profiles['user2'].name}
        </button>
      </div>
    </div>
  );
};

export default MatchupPage;
