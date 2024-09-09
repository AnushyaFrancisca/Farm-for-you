import '../css/about.css';
import Homepg from '../Components/Homepg';
import Aboutpg from '../Components/aboutpg';
import Work from '../Components/Work';
import Testimonial from '../Components/Testimonial';
import Contact from '../Components/Contact';
import Footer from '../Components/Footer';

function About() {
  return (
    <div className="App">
      <Homepg />
      <Aboutpg />
      <Work />
      <Testimonial />
      <Contact />
      <Footer />
    </div>
  );
}

export default About;