// Parallax scrolling functionality
window.addEventListener('scroll', function () {
  const containerWrapper = document.querySelector('.container-wrapper');
  if (containerWrapper) {
    const scrollPosition = window.scrollY;
    containerWrapper.style.backgroundPositionY = `${scrollPosition * 0.5}px`; // Adjust multiplier for parallax speed
  }
});

// Carousel functionality
function initCarousel(carouselId) {
  const carousel = document.getElementById(carouselId);
  if (carousel) {
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
}

// Initialize carousels
document.addEventListener('DOMContentLoaded', function () {
  initCarousel('carouselCollege');
  initCarousel('carouselStudents');
});

// Student Life carousel
let studentLifeIndex = 0;

function showStudentLifeSlide(index) {
  const slides = document.querySelectorAll('.student-life-slide');
  if (slides.length > 0) {
    slides.forEach((slide, i) => {
      slide.style.display = i === index ? 'block' : 'none';
    });
  }
}

function nextStudentLifeSlide() {
  const slides = document.querySelectorAll('.student-life-slide');
  if (slides.length > 0) {
    studentLifeIndex = (studentLifeIndex + 1) % slides.length;
    showStudentLifeSlide(studentLifeIndex);
  }
}

function prevStudentLifeSlide() {
  const slides = document.querySelectorAll('.student-life-slide');
  if (slides.length > 0) {
    studentLifeIndex = (studentLifeIndex - 1 + slides.length) % slides.length;
    showStudentLifeSlide(studentLifeIndex);
  }
}

setInterval(() => {
  nextStudentLifeSlide();
}, 5000);

document.addEventListener('DOMContentLoaded', () => {
  showStudentLifeSlide(studentLifeIndex);
});

// Carousel 3 functionality
document.addEventListener('DOMContentLoaded', () => {
  const carouselItems = document.querySelector('.carousel-items');
  const nextButton = document.querySelector('.carousel-next');

  if (carouselItems && nextButton) {
    let currentIndex = 0;

    nextButton.addEventListener('click', () => {
      const items = document.querySelectorAll('.carousel-item');
      if (items.length > 0) {
        currentIndex = (currentIndex + 1) % items.length;
        const offset = -currentIndex * 100;
        carouselItems.style.transform = `translateX(${offset}%)`;
      }
    });
  }
});

// Carousel 4 functionality
document.addEventListener('DOMContentLoaded', () => {
  const track = document.querySelector('.carousel-track');
  const prevButton = document.querySelector('.admin-carousel-prev');
  const nextButton = document.querySelector('.admin-carousel-next');

  if (track && prevButton && nextButton) {
    const items = Array.from(track.children);
    let currentIndex = 0;

    const updateCarouselPosition = () => {
      const itemWidth = items[0].getBoundingClientRect().width;
      track.style.transform = `translateX(-${currentIndex * itemWidth}px)`;
    };

    nextButton.addEventListener('click', () => {
      if (currentIndex < items.length - 1) {
        currentIndex++;
      } else {
        currentIndex = 0;
      }
      updateCarouselPosition();
    });

    prevButton.addEventListener('click', () => {
      if (currentIndex > 0) {
        currentIndex--;
      } else {
        currentIndex = items.length - 1;
      }
      updateCarouselPosition();
    });

    window.addEventListener('resize', updateCarouselPosition);
  }
});

// Department carousel
document.addEventListener('DOMContentLoaded', () => {
  const departmentsLinks = document.querySelectorAll('.departments-links ul li a');
  const carouselItem = document.querySelector('.department-carousel-item');
  const professorData = {
    silviculture: {
      img: "/static/images/professor-images/dean-image.jpg",
      name: 'Dr. Milkuri Chiranjeeva Reddy',
      details: `
        Dr. Chiranjeeva has more than six years of research and teaching experience. 
        He obtained his Doctorate in Forestry with specialization in Silviculture and 
        a master’s degree in forestry with specialization in Plantation technology.
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
  };

  departmentsLinks.forEach(link => {
    link.addEventListener('click', event => {
      event.preventDefault();
      const departmentId = event.target.getAttribute('href').replace('#', '');

      if (professorData[departmentId]) {
        const { img, name, details, link } = professorData[departmentId];

        if (carouselItem) {
          carouselItem.querySelector('.professor-image').src = img;
          carouselItem.querySelector('h3').textContent = name;
          carouselItem.querySelector('p').innerHTML = details;
          carouselItem.querySelector('.read-more').href = link;
        }
      }
    });
  });
});

// Menu visibility toggle
document.addEventListener('DOMContentLoaded', function () {
  const toggleButton = document.querySelector('.menu-toggle');
  const navLinks = document.querySelector('.nav-links');

  if (toggleButton && navLinks) {
    toggleButton.addEventListener('click', function () {
      navLinks.classList.toggle('active');
    });
  }
});

// Chatbot logic
document.addEventListener('DOMContentLoaded', function () {
  const responses = {
    "hi": "Hello! How can I help you today?",
    "admission": "Admissions are open. You can apply online through our portal.",
    "courses": "We offer courses in Forestry, Environmental Science, and Wildlife Studies.",
    "contact": "You can contact us at info@forestcollege.edu or call 123-456-7890."
  };

  const sendButton = document.getElementById('send-button');
  const chatbox = document.getElementById('chatbox');
  const userInput = document.getElementById('user-input');

  if (sendButton && chatbox && userInput) {
    sendButton.addEventListener('click', function () {
      const userMessage = userInput.value.trim().toLowerCase();

      if (userMessage === '') return;

      const userMessageDiv = document.createElement('div');
      userMessageDiv.textContent = `You: ${userMessage}`;
      chatbox.appendChild(userMessageDiv);

      const botResponse = responses[userMessage] || "I'm sorry, I didn't understand that. Can you rephrase?";
      const botMessageDiv = document.createElement('div');
      botMessageDiv.textContent = `Bot: ${botResponse}`;
      botMessageDiv.style.color = 'blue';
      chatbox.appendChild(botMessageDiv);

      userInput.value = '';
      chatbox.scrollTop = chatbox.scrollHeight;
    });
  }
});
