import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './Home';
import SignUp from './SignUp/SignUp';
import SignIn from './SignIn/SignIn';
<<<<<<< HEAD
import Dashboard from './Dashboard/Dashboard';
// import About from './About';
=======
import About from './About';
>>>>>>> 5a628a35b6b86ca9d3cb425871d1fcb06a73d4c3
import logo from '../images/logo.svg'; // Update the path to where your logo.svg is located
import '../css/App.css'; // Update the path to where your App.css is located

function App() {
  return (
    <Router>
      <div>
        <Routes>
          {/* <Route path="/" element={<Home />} /> */}
          <Route path="/signup" element={<SignUp />} />
          <Route path="/signin" element={<SignIn />} /> 
          {/* <Route path="/" element={<Dashboard />} />   */}
          {/* <Route path="/about" element={<About />} /> */}

        </Routes>
      </div>
    </Router>
  );
}

export default App;
