import React from 'react';
import { Link } from 'react-router-dom'; // Import Link for navigation
import '../css/Home.css'; // Adjust the path if necessary
import myImage from '../images/bg-img.png'; // Adjust the path to your image
import cloudImage from '../images/clouds.png'; // The cloud image you want to use
import logo from '../images/logo1.png'; 
import Header from '../Components/Header';

function Home() {
  return (
    <div className="home-container" style={{ backgroundImage: `url(${myImage})` }}>
      <img src={cloudImage} alt="Moving Clouds" className="moving-clouds" />

      {/* Main Content */}
      <div className="content" style={{ position: 'relative', zIndex: 2 }}>
         <Header />

         <img 
          src={logo} 
          alt="Logo" 
          style={{ 
            position: 'absolute', 
            top: '-20px', 
            left: '65px', 
            transform: 'translate(-50%, -50%)',
            width: '700px', // Set the width you want
            height: 'auto' // This maintains aspect ratio
          }} 
        />

        {/* Learn More Button
        <button className="learn-more-button">
        <Link to="/about">Learn More</Link>
        </button> */}
      </div>
    </div>
  );
}

export default Home;
