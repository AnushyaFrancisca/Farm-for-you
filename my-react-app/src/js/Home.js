import React from 'react';
import '../css/Home.css'; // Adjust the path if necessary
import myImage from '../images/bg-img.png'; // Adjust the path to your image
import cloudImage from '../images/clouds.png'; // The cloud image you want to use


function Home() {
  return (
    <div className="home-container" style={{ backgroundImage: `url(${myImage})` }}>
      <img src={cloudImage} alt="Moving Clouds" className="moving-clouds" />

      {/* Main Content */}
      <div className="content" style={{ position: 'relative', zIndex: 2 }}>
        <h1>Welcome to the Home Page</h1>
      </div>
    </div>
  );
}


export default Home;
