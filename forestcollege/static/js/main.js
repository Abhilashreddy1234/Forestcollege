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
// Department data with descriptions and image paths
const departmentDescriptions = {
  "Silviculture and Agroforestry": "Telangana state is blessed with rich biodiversity and wildlife forms are an important part of it. For the protection and conservation of wildlife, various protected areas are established in the state. Habitat fragmentation and degradation are the major issues in the conservation of wildlife. Natural resources are facing enormous pressure, resulting in the decline of wildlife over the years, with many more species being threatened with extinction. Deep knowledge of the different components of the ecology of species and itsSilviculture is the practice of controlling the establishment, growth, composition, health, and quality of forests to meet diverse needs and values.",
  "Natural Resource Management and Conservation": "Focuses on sustainable management and conservation of natural resources like soil, water, and biodiversity.",
  "Wildlife and Habitat Management": "Involves the preservation and management of wildlife habitats and species.",
  "Forest Products and Utilization": "Covers the development and management of forest-based products and their efficient utilization.",
  "Tree Breeding and Improvement": "Aims to enhance the genetic potential and productivity of tree species.",
  "Forest Ecology and Climate Science": "Studies the relationship between forests and climate, focusing on ecological conservation.",
  "Basic and Social Sciences": "Explores the interplay between forestry, social sciences, and basic sciences for sustainable development."
};

function showDepartment(department, image) {
  const info = departmentDescriptions[department] || "Information not available.";
  document.getElementById("department-info").textContent = info;
  document.getElementById("department-image").src = image;
}
// laboratories //
const laboratoryDescriptions = {
  "Chemistry Laboratory": "The Chemistry Laboratory is equipped with modern instruments and facilities for conducting research and experiments in organic, inorganic, and physical chemistry.",
  "Physics Laboratory": "The Physics Laboratory focuses on advanced research in quantum mechanics, thermodynamics, and electromagnetism.",
  "Biotechnology Laboratory": "The Biotechnology Laboratory supports experiments in genetic engineering, microbiology, and molecular biology.",
  "Soil Testing Laboratory": "The Soil Testing Laboratory provides analysis and research on soil fertility and composition for sustainable agriculture."
};

function showLaboratory(laboratory, image) {
  const info = laboratoryDescriptions[laboratory] || "Information not available.";
  document.getElementById("laboratory-info").textContent = info;
  document.getElementById("laboratory-image").src = image;
}
// studentAchievements table  //
            document.querySelectorAll('.toggle-dropdown').forEach(header => {
              header.addEventListener('click', () => {
                const dropdown = header.nextElementSibling;
                dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
              });
            });
// forest museum //
let currentSlide = 0;

function showSlide(index) {
  const slides = document.querySelectorAll('.carousel-image');
  slides.forEach((slide, idx) => {
    slide.classList.toggle('active', idx === index);
  });
}

function nextSlide() {
  const slides = document.querySelectorAll('.carousel-image');
  currentSlide = (currentSlide + 1) % slides.length;
  showSlide(currentSlide);
}

function prevSlide() {
  const slides = document.querySelectorAll('.carousel-image');
  currentSlide = (currentSlide - 1 + slides.length) % slides.length;
  showSlide(currentSlide);
}

// Initialize the first slide
showSlide(currentSlide);
// cif //
const instrumentData = {
  hplc: {
    image: "images\services-images\CIF1IMAGE.jpg",
    details: `
      <table>
        <tr>
          <th>Equipment Available</th>
          <th>Charges for Govt Universities/Institutes</th>
          <th>Charges for Private Industry/Institutes</th>
        </tr>
        <tr>
          <td>High-Performance Liquid Chromatography</td>
          <td>2000/- per sample + GST 18%</td>
          <td>3000/- per sample + GST 18%</td>
        </tr>
      </table>
    `
  },
  gc: {
    image: "gc.jpg",
    details: `
      <table>
        <tr>
          <th>Equipment Available</th>
          <th>Charges for Govt Universities/Institutes</th>
          <th>Charges for Private Industry/Institutes</th>
        </tr>
        <tr>
          <td>Gas Chromatograph with Flame Ionization Detector (Nexis 2030)</td>
          <td>2000/- per sample + GST 18%</td>
          <td>3000/- per sample + GST 18%</td>
        </tr>
      </table>
    `
  },
  // Add more instruments following the same format...
};

function showInstrumentDetails(instrumentKey) {
  const instrument = instrumentData[instrumentKey];
  if (instrument) {
    document.getElementById("instrument-image").src = instrument.image;
    document.getElementById("instrument-details").innerHTML = instrument.details;
  }
}

