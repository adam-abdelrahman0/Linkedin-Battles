import React, { useState, useEffect } from "react";
import axios from "axios";

const UserPage = () => {
  const [User, setUser] = useState([]);

  useEffect(() => {
    axios.get(`127.0.0.1/api/users/all`)
      .then((res) => setUser(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div>
      <h2>User</h2>
      <p>{User}</p>
    </div>
  );
};

export default UserPage;
