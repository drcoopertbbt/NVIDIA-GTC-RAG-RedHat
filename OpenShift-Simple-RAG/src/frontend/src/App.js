import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('/ask', { prompt });
      setResponse(JSON.stringify(res.data, null, 2));
    } catch (error) {
      console.error('Error fetching response:', error);
      setResponse('Error fetching response');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h2>Ask a Question</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Enter your prompt"
          />
          <button type="submit">Submit</button>
        </form>
        <h3>Response:</h3>
        <pre>{response}</pre>
      </header>
    </div>
  );
}

export default App;