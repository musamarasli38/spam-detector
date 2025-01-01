import React, { useState } from 'react';
import { predictComment } from './api';
import REACT_APP_RECAPTCHA_SECRET_KEY from '@env/RECAPTCHA_SECRET_KEY';

function App() {
  const [comment, setComment] = useState('');
  const [prediction, setPrediction] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const token = await window.grecaptcha.execute(REACT_APP_RECAPTCHA_SECRET_KEY, { action: 'submit' });

      const response = await fetch('/predict', {
        comment: 'This is a test comment',
        recaptcha_token: token,
      })

      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
    const result = await predictComment(comment);
    setPrediction(result);
  };

  return (
    <div style={{ padding: '2rem', textAlign: 'center' }}>
      <h1>Spam Comment Detector</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={comment}
          onChange={(e) => setComment(e.target.value)}
          placeholder="Enter your comment here"
          rows="4"
          cols="50"
        />
        <br />
        <button type="submit">Check Comment</button>
      </form>
      {prediction && (
        <div style={{ marginTop: '1rem' }}>
          <h2>Result:</h2>
          <p><strong>Comment:</strong> {prediction.comment}</p>
          <p><strong>Prediction:</strong> {prediction.prediction}</p>
        </div>
      )}
    </div>
  );
}

export default App;
