import axios from 'axios';

const api = axios.create({
    baseURL: 'http://127.0.0.1:5000',
    headers: {
        'Content-Type': 'application/json',
    },
});

export const predictComment = async (comment) => {
    try {
        const response = await api.post('/predict', { comment });
        return response.data;
    } catch (error) {
        console.error('Error predicting comment:', error);
        throw error;
    }
};
