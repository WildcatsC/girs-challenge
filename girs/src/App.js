import React from 'react';
import {BrowserRouter as Router, Route, Routes} from "react-router-dom";

import Login from "./components/Login/Login";
import Display from "./components/Display/Display";


function App() {
  return (
    <Router>
      <Routes>
        <Route path = "/" element = {<Login/>} />
        <Route path = "display" element = {<Display />}/>
      </Routes>
    </Router>
    
  );
}

export default App;
