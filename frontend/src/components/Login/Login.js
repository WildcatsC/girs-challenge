import {React, useState} from "react";
import { Link } from "react-router-dom";
import {BrowserRouter as Router, Route, Routes} from "react-router-dom";

import pairs from './auth';
import './Login.css';

function Header() {
    // Import result is the URL of your image
    return 
  }


const Login = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [cred, setCred] = useState(false);

    const auth = () => {
        if (pairs[username] === password) {
            setCred(true);
            return true;
        };
        console.log(cred);
        alert('Invalid username or password');
        return false;
    };

    console.log(cred);
    
    
    return (
        <div className="login-window">
            <img src={require('./girs-banner.png')} id='banner'/>
            <input id = 'username' placeholder="Username..." onChange={(event)=>setUsername(event.target.value)}></input>
            <input id = 'password' placeholder="Password..." onChange={(event)=>setPassword(event.target.value)}></input>
            <Link id = 'login' onClick = {e=>auth()?null:e.preventDefault()} to = {{pathname : `/display?name=${username}`}} state = {{au : cred}}>
                login
            </Link>
        </div>
    );
    
}
export default Login;