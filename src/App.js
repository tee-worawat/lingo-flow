import React from 'react';
import Block from './Block';
import Connection from './Connection';
import './App.css';

function App() {
  return (
    <div className="App">
      <h1>AI Block Software Development</h1>
      <div className="blocks-container">
        <Block id="block1" />
        <Block id="block2" />
        <Connection from="block1" to="block2" />
      </div>
    </div>
  );
}

export default App;
