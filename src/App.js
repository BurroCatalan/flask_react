import React, { Component, useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

const [currentUser, setCurrentUser] = useState(0);

  useEffect(() => {
    fetch('/user').then(res => res.json()).then(data => {
      setCurrentUser(data.user);
    });
  }, []);
  return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React you fool</h2>
        </div>
<p>The current time is {currentTime}.</p>
<p>The user is {currentUser}.</p>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }

export default App;
