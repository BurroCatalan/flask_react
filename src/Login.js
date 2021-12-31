import "./styles.css";
import React from "react";
import { UserContext } from "./App.js";

export default function Login() {
  const username = React.useRef();
  const password = React.useRef();
  const currentUser = React.useContext(UserContext);

  const onSubmit = (ev) => {
    ev.preventDefault();
    console.log(username.current.value);
    if (username.current.value == null || username.current.value === "")  {
      currentUser.logoutUser();
      console.log("LEER!");
    } else {
      currentUser.loginUser(username.current.value);
      console.log("NichtLeer!");
    }
  };

  return (
    <div>
      {currentUser.username == null ? (
        <form onSubmit={onSubmit}>
          <table>
            <tbody>
              <tr>
                <td>
                  <label className="Label" type="Login">
                    User:
                  </label>
                </td>
                <td>
                  <input className="Input" type="text" ref={username} />
                </td>
              </tr>
              <tr>
                <td>
                  <label className="Label" type="Password">
                    Password:
                  </label>
                </td>
                <td>
                  <input className="Password" type="password" ref={password} />
                </td>
              </tr>
              <tr>
                <td />
                <td>
                  <input className="SubmitButton" type="submit" value="Login" />
                </td>
              </tr>
            </tbody>
          </table>
        </form>
      ) : (
        <button onClick={currentUser.logoutUser}>Logout</button>
      )}
    </div>
  );
}
