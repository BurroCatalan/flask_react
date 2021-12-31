import "./styles.css";
import Login from "./Login.js";
import React from "react";
import { UserContext } from "./App.js";

export default function Navigation() {
  const currentUser = React.useContext(UserContext);

  return (
    <div className="Navigation">
      {currentUser.username ? (
        <p>Welcome, {currentUser.username}!</p>
      ) : (
        <p>Please login</p>
      )}
      <Login />
    </div>
  );
}