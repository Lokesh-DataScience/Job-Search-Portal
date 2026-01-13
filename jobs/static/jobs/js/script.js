// ==========================
// DOM READY
// ==========================
document.addEventListener("DOMContentLoaded", () => {
  initMenu();
  initJobFilters();
  initSearch();
  initCTAForm();
  initSwipers();
  initSmoothScroll();
});

// ==========================
// MOBILE MENU TOGGLE
// ==========================
function initMenu() {
  const hamburger = document.querySelector(".hamburger");
  const navMenu = document.querySelector(".nav-menu");

  if (!hamburger || !navMenu) return;

  hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
  });

  // Close menu on link click
  document.querySelectorAll(".nav-link").forEach(link => {
    link.addEventListener("click", () => {
      navMenu.classList.remove("active");
      hamburger.classList.remove("active");
    });
  });
}

// ==========================
// JOB FILTER BUTTONS
// ==========================
function initJobFilters() {
  const filterButtons = document.querySelectorAll(".filter-btn");
  const jobCards = document.querySelectorAll(".job-card");

  filterButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      // Active state
      filterButtons.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      const filter = btn.textContent.trim().toLowerCase();

      jobCards.forEach(card => {
        const jobType = card.querySelector(".job-type")?.textContent.toLowerCase();

        if (filter === "all jobs" || jobType?.includes(filter)) {
          card.style.display = "block";
        } else {
          card.style.display = "none";
        }
      });
    });
  });
}

// ==========================
// SEARCH BUTTON (DEMO)
// ==========================
function initSearch() {
  const searchBtn = document.querySelector(".search-btn");
  const searchInput = document.querySelector(".search-input");

  if (!searchBtn || !searchInput) return;

  searchBtn.addEventListener("click", () => {
    const query = searchInput.value.trim();

    if (!query) {
      alert("Please enter a job title or keyword");
      return;
    }

    alert(`Searching jobs for: "${query}"`);
  });
}

// ==========================
// CTA EMAIL FORM
// ==========================
function initCTAForm() {
  const form = document.querySelector(".cta-form");
  const emailInput = document.querySelector(".cta-input");

  if (!form || !emailInput) return;

  form.addEventListener("submit", e => {
    e.preventDefault();

    const email = emailInput.value.trim();

    if (!validateEmail(email)) {
      alert("Please enter a valid email address");
      return;
    }

    alert("Thank you for joining JobNexus 🚀");
    emailInput.value = "";
  });
}

function validateEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

// ==========================
// SWIPER SLIDERS
// ==========================
function initSwipers() {
  // Companies slider
  new Swiper(".companies-slider", {
    slidesPerView: 1,
    spaceBetween: 20,
    loop: true,
    pagination: {
      el: ".companies-slider .swiper-pagination",
      clickable: true
    },
    breakpoints: {
      640: { slidesPerView: 2 },
      1024: { slidesPerView: 4 }
    }
  });

  // Testimonials slider
  new Swiper(".testimonials-slider", {
    slidesPerView: 1,
    loop: true,
    autoplay: {
      delay: 4000,
      disableOnInteraction: false
    },
    pagination: {
      el: ".testimonials-slider .swiper-pagination",
      clickable: true
    }
  });
}

// ==========================
// SMOOTH SCROLL
// ==========================
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
      const target = document.querySelector(this.getAttribute("href"));
      if (!target) return;

      e.preventDefault();
      target.scrollIntoView({ behavior: "smooth" });
    });
  });
}
