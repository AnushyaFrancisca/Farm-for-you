import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './Home';
import SignUp from './SignUp';
import About from './About';
import logo from '../images/logo.svg'; // Update the path to where your logo.svg is located
import '../css/App.css'; // Update the path to where your App.css is located

function App() {
  return (
    <Router>
      <div>
        <Routes>
          {/* <Route path="/" element={<Home />} /> */}
          <Route path="/signup" element={<SignUp />} />
          <Route path="/" element={<About />} />
          

        </Routes>
      </div>
    </Router>
  );
}

export default App;
