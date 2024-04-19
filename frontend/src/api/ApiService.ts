// ApiService.tsx


const BASE_URL = 'http://localhost:8000';

export const fetchEvents = async () => {
  try {
    const response = await fetch(`${BASE_URL}/event`);
    if (!response.ok) {
      throw new Error('Failed to fetch events');
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching events:', error);
    throw error;
  }
};
