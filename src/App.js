import "./styles.css";
import Navigation from "./Navigation.js";
import React, { useState, useEffect } from 'react';

export const UserContext = React.createContext();

export default function App() {
  const [username, setUsername] = React.useState(null);
  const [currentTime, setCurrentTime] = useState(null);
  const [userToken, setUserToken] = useState(null);
  const [apiUser, setapiUser] = useState(null);

  useEffect(() => {
    fetch('/api/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  useEffect(() => {
    fetch('/api/login').then(res => res.json()).then(data => {
      setUserToken(data.token);
    });
  }, []);

  const currentUser = {
    username: username,
    loginUser: (_username) => {
      setUsername(_username);
    },
    logoutUser: () => {
      setUsername(null);
    }
  };

  return (
    <div className="App">
      <h1>Hello CodeSandbox</h1>
      <h2>Start editing to see some magic happen!</h2>
      <p>The current time is {currentTime}.</p>
      <p>The token for {username} is {token}.</p>
      <UserContext.Provider value={currentUser}>
        <Navigation />
      </UserContext.Provider>
    </div>
  );
}