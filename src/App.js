import "./styles.css";
import Navigation from "./Navigation.js";
import React from "react";

export const UserContext = React.createContext();

export default function App() {
  const [username, setUsername] = React.useState(null);
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/api/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
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
      <UserContext.Provider value={currentUser}>
        <Navigation />
      </UserContext.Provider>
    </div>
  );
}