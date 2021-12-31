import "./styles.css";
import { UserContext } from "./App.js";
import PropTypes from 'prop-types';
import React, {useRef} from 'react';

async function loginUser(credentials) {
    return fetch('burropi:5000/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(credentials)
    })
      .then(data => data.json())
   }

export default function Login({ setToken }) {
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

  const handleSubmit = async e => {
    e.preventDefault();
    const token = await loginUser({
      username,
      password
    });
    setToken(token);
    console.log(token)
  }

  
Login.propTypes = {
    setToken: PropTypes.func.isRequired
  }


  return (
    <div>
      {currentUser.username == null ? (
        <form onSubmit={handleSubmit}>
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
