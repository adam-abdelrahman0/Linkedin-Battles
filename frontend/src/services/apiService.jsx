import axios from 'axios';

// API calls (example)
export const getUserData = async () => {
  try {
    const response = await axios.get(`${VITE_BACKEND_URL}/api/user/data`);
    return response.data;
  } catch (error) {
    console.error('Error fetching user data:', error);
    throw error;
  }
};

// Example POST request
export const createUser = async (userData) => {
  try {
    const response = await axios.post(`${VITE_BACKEND_URL}/api/user`, userData);
    return response.data;
  } catch (error) {
    console.error('Error creating user:', error);
    throw error;
  }
};
