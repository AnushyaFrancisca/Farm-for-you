import React from 'react';
import { Link } from 'react-router-dom'; // Import Link for navigation
import './Header.css'; // Import the CSS file

function Header() {
  return (
    <div className="header-wrapper"> {/* New container for the header */}
      <header className="header-container">
        <nav className="navbar">
          <Link to="/" className="active">Home</Link>
          <Link to="/about">About Us</Link>
          <Link to="/signin">Login</Link>
          <Link to="/signup">Sign Up</Link>        </nav>
      </header>
    </div>
  );
}

export default Header;
