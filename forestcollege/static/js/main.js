// Parallax scrolling functionality
window.addEventListener('scroll', function () {
  const containerWrapper = document.querySelector('.container-wrapper');
  const scrollPosition = window.scrollY;

  // Adjust the background position for the parallax effect
  containerWrapper.style.backgroundPositionY = `${scrollPosition * 0.5}px`; // Adjust multiplier for parallax speed
});

// Carousel functionality
function initCarousel(carouselId) {
  const carousel = document.getElementById(carouselId);
  const images = carousel.querySelectorAll('img');
  let currentIndex = 0;

  function showImage(index) {
    images.forEach((img, i) => {
      img.classList.toggle('active', i === index);
    });
  }

  // Automatically cycle through images
  setInterval(() => {
    currentIndex = (currentIndex + 1) % images.length;
    showImage(currentIndex);
  }, 3000);

  // Show the first image initially
  showImage(currentIndex);
}

// Initialize carousels
document.addEventListener('DOMContentLoaded', function () {
  initCarousel('carouselCollege');
  initCarousel('carouselStudents');
});



let studentLifeIndex = 0;

function showStudentLifeSlide(index) {
    const slides = document.querySelectorAll('.student-life-slide');
    slides.forEach((slide, i) => {
        slide.style.display = i === index ? 'block' : 'none';
    });
}

// Next Slide
function nextStudentLifeSlide() {
    const slides = document.querySelectorAll('.student-life-slide');
    studentLifeIndex = (studentLifeIndex + 1) % slides.length;
    showStudentLifeSlide(studentLifeIndex);
}

// Previous Slide
function prevStudentLifeSlide() {
    const slides = document.querySelectorAll('.student-life-slide');
    studentLifeIndex = (studentLifeIndex - 1 + slides.length) % slides.length;
    showStudentLifeSlide(studentLifeIndex);
}

// Auto-cycle slides every 5 seconds
setInterval(() => {
    nextStudentLifeSlide();
}, 5000);

// Initialize the carousel on page load
document.addEventListener('DOMContentLoaded', () => {
    showStudentLifeSlide(studentLifeIndex);
});
// 3rd carousal //
document.addEventListener('DOMContentLoaded', () => {
  const carouselItems = document.querySelector('.carousel-items');
  const nextButton = document.querySelector('.carousel-next');
  let currentIndex = 0;

  nextButton.addEventListener('click', () => {
    const items = document.querySelectorAll('.carousel-item');
    currentIndex = (currentIndex + 1) % items.length;
    const offset = -currentIndex * 100;
    carouselItems.style.transform = `translateX(${offset}%)`;
  });
});
// 4h carousal 
// JavaScript for Carousel Functionality
document.addEventListener("DOMContentLoaded", () => {
  const track = document.querySelector(".carousel-track");
  const items = Array.from(track.children);
  const prevButton = document.querySelector(".admin-carousel-prev");
  const nextButton = document.querySelector(".admin-carousel-next");

  let currentIndex = 0;

  // Function to update carousel position
  const updateCarouselPosition = () => {
      const itemWidth = items[0].getBoundingClientRect().width;
      track.style.transform = `translateX(-${currentIndex * itemWidth}px)`;
  };

  // Function to move to the next item
  const moveToNext = () => {
      if (currentIndex < items.length - 1) {
          currentIndex++;
      } else {
          currentIndex = 0; // Reset to the first item
      }
      updateCarouselPosition();
  };

  // Function to move to the previous item
  const moveToPrev = () => {
      if (currentIndex > 0) {
          currentIndex--;
      } else {
          currentIndex = items.length - 1; // Go to the last item
      }
      updateCarouselPosition();
  };

  // Attach event listeners to buttons
  nextButton.addEventListener("click", moveToNext);
  prevButton.addEventListener("click", moveToPrev);

  // Ensure the carousel works on window resize
  window.addEventListener("resize", updateCarouselPosition);
});

// 5th carousal 
// JavaScript to handle department clicks and update carousel details
document.addEventListener('DOMContentLoaded', () => {
  const departmentsLinks = document.querySelectorAll('.departments-links ul li a');
  const carouselItem = document.querySelector('.department-carousel-item');
  const professorData = {
    silviculture: {
      img:"/static/images/professor-images/dean-image.jpg",
      name: 'Dr. Milkuri Chiranjeeva Reddy',
      details: `
        Dr. Chiranjeeva has more than six years of research and teaching experience. 
        He obtained his Doctorate in Forestry with specialization in Silviculture and 
        a master’s degree in forestry with specialization in Plantation technology.
        <br><br>
        He has obtained Junior Research Fellowship from the Indian Council of Agricultural Research for the year 2010-2012.
      `,
      link: 'dr-chiranjeeva-profile.html',
    },
    'natural-resource': {
      img: 'professor2.jpg',
      name: 'Dr. John Smith',
      details: `
        Dr. John Smith specializes in Natural Resource Management and has a track record 
        of over 10 years in environmental conservation and research.
      `,
      link: 'dr-john-profile.html',
    },
    // Add more departments with their corresponding professor details
  };

  departmentsLinks.forEach(link => {
    link.addEventListener('click', event => {
      event.preventDefault();
      const departmentId = event.target.getAttribute('href').replace('#', '');
      
      if (professorData[departmentId]) {
        const { img, name, details, link } = professorData[departmentId];
        
        // Update carousel content
        carouselItem.querySelector('.professor-image').src = img;
        carouselItem.querySelector('h3').textContent = name;
        carouselItem.querySelector('p').innerHTML = details;
        carouselItem.querySelector('.read-more').href = link;
      }
    });
  });
});
// menu visibility //
document.addEventListener('DOMContentLoaded', function () {
  const toggleButton = document.querySelector('.menu-toggle');
  const navLinks = document.querySelector('.nav-links');

  toggleButton.addEventListener('click', function () {
      navLinks.classList.toggle('active');
  });
});