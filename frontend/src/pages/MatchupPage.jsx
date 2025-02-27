import React, { useState, useEffect } from "react";
import axios from "axios";

const MatchupPage = () => {
  const [profiles, setProfiles] = useState(null);

  useEffect(() => {
    axios.get(`${import.meta.env.VITE_BACKEND_URL}/matchup`)
      .then((res) => setProfiles(res.data))
      .catch((err) => console.error(err));
  }, []);

  const handleVote = (winnerId, loserId) => {
    axios.post(`${import.meta.env.VITE_BACKEND_URL}/vote`, {
      winner_id: winnerId,
      loser_id: loserId,
    }).then(() => window.location.reload());
  };

  if (!profiles) return <p>Loading...</p>;

  return (
    <div>
      <h2>Which LinkedIn profile is better?</h2>
      <div>
        <button onClick={() => handleVote(profiles[0].id, profiles[1].id)}>
          {profiles[0].summary}
        </button>
        <span> VS </span>
        <button onClick={() => handleVote(profiles[1].id, profiles[0].id)}>
          {profiles[1].summary}
        </button>
      </div>
    </div>
  );
};

export default MatchupPage;
