// assets/js/main.js – Handles theme, RTL, menu, back-to-top, auth features, and validation
// <link href="assets/css/dark-mode.css" rel="stylesheet" id="dark-mode-stylesheet" disabled>
// <link href="assets/css/rtl.css" rel="stylesheet" id="rtl-stylesheet" disabled> back-to-top

// Utility to set data attribute and persist in localStorage
function setTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('theme', theme);
  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) themeToggle.textContent = theme === 'dark' ? '☀️' : '🌙';
  // Enable/disable dark-mode stylesheet
  const dmLink = document.getElementById('dark-mode-stylesheet');
  if (dmLink) dmLink.disabled = (theme !== 'dark');
}

function initTheme() {
  const saved = localStorage.getItem('theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const theme = saved || (prefersDark ? 'dark' : 'light');
  setTheme(theme);
}

function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme');
  setTheme(current === 'dark' ? 'light' : 'dark');
}

function setDirection(dir) {
  document.documentElement.setAttribute('dir', dir);
  localStorage.setItem('dir', dir);
  const rtlToggle = document.getElementById('rtl-toggle');
  if (rtlToggle) rtlToggle.textContent = dir === 'rtl' ? 'LTR' : 'RTL';
  // Enable/disable RTL stylesheet
  const rtlLink = document.getElementById('rtl-stylesheet');
  if (rtlLink) rtlLink.disabled = (dir !== 'rtl');
}

function initDirection() {
  const saved = localStorage.getItem('dir') || 'ltr';
  setDirection(saved);
}

function toggleDirection() {
  const current = document.documentElement.getAttribute('dir') || 'ltr';
  setDirection(current === 'ltr' ? 'rtl' : 'ltr');
}

// Off-canvas menu for small screens
function initMenu() {
  const menu = document.getElementById('nav-menu');
  const toggle = document.getElementById('menu-toggle');
  if (toggle && menu) {
    toggle.addEventListener('click', () => {
      menu.classList.toggle('open');
    });
    // Close menu when a link is clicked (mobile)
    menu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => menu.classList.remove('open'));
    });
  }
}

// Back-to-top button
function initBackToTop() {
  const btn = document.getElementById('back-to-top');
  if (btn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 300) {
        btn.classList.add('show');
      } else {
        btn.classList.remove('show');
      }
    });
    btn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
}

// Lightbox initialization
function initLightbox() {
  const modal = document.getElementById('lightbox-modal');
  if (!modal) return;
  
  const modalImg = document.getElementById('lightbox-image');
  const modalCaption = document.getElementById('lightbox-caption');
  const closeBtn = document.getElementById('lightbox-close');
  
  const galleryItems = document.querySelectorAll('.gallery-item');
  galleryItems.forEach(item => {
    item.addEventListener('click', () => {
      const img = item.querySelector('img');
      const largeSrc = item.getAttribute('data-lightbox-src') || (img ? img.src : '');
      const captionText = item.getAttribute('data-lightbox-caption') || (img ? img.alt : '');
      
      if (modalImg) modalImg.src = largeSrc;
      if (modalCaption) modalCaption.textContent = captionText;
      
      modal.classList.add('show');
      document.body.style.overflow = 'hidden'; // prevent scrolling behind
    });
  });
  
  const closeModal = () => {
    modal.classList.remove('show');
    document.body.style.overflow = '';
  };
  
  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  modal.addEventListener('click', (e) => {
    if (e.target === modal || e.target.closest('.lightbox-close')) {
      closeModal();
    }
  });
  
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('show')) {
      closeModal();
    }
  });
}

// Password visibility toggles
function initPasswordToggles() {
  const toggleBtns = document.querySelectorAll('.password-toggle-btn');
  toggleBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const inputId = btn.getAttribute('data-target');
      const input = document.getElementById(inputId);
      if (input) {
        const isPassword = input.type === 'password';
        input.type = isPassword ? 'text' : 'password';
        btn.textContent = isPassword ? '🙈' : '👁️';
        btn.setAttribute('aria-label', isPassword ? 'Hide password' : 'Show password');
      }
    });
  });
}

// Form validation with tooltips
function initFormValidation() {
  const forms = document.querySelectorAll('form');
  forms.forEach(form => {
    // Validate on submit
    form.addEventListener('submit', (e) => {
      if (!form.checkValidity()) {
        e.preventDefault();
        e.stopPropagation();
      }
      form.classList.add('was-validated');
    });

    // Validate individual fields on blur and input
    const inputs = form.querySelectorAll('input, select, textarea');
    inputs.forEach(input => {
      input.addEventListener('blur', () => validateField(input));
      input.addEventListener('input', () => {
        if (input.classList.contains('is-invalid') || input.classList.contains('is-valid')) {
          validateField(input);
        }
      });
    });
  });
}

function validateField(input) {
  const isValid = input.checkValidity();
  
  if (isValid) {
    input.classList.remove('is-invalid');
    input.classList.add('is-valid');
    // Remove any existing tooltip
    const existingTooltip = input.parentElement.querySelector('.invalid-tooltip');
    if (existingTooltip) existingTooltip.remove();
  } else {
    input.classList.remove('is-valid');
    input.classList.add('is-invalid');
    
    // Create tooltip if it doesn't exist
    let tooltip = input.parentElement.querySelector('.invalid-tooltip');
    if (!tooltip) {
      tooltip = document.createElement('div');
      tooltip.className = 'invalid-tooltip';
      input.parentElement.appendChild(tooltip);
    }
    tooltip.textContent = input.validationMessage || 'Please fill out this field.';
  }
}

// Booking form initialization
function initBookingForm() {
  const dateInput = document.getElementById('date');
  if (dateInput) {
    // Set minimum date to today
    const today = new Date();
    const yyyy = today.getFullYear();
    const mm = String(today.getMonth() + 1).padStart(2, '0');
    const dd = String(today.getDate()).padStart(2, '0');
    dateInput.min = `${yyyy}-${mm}-${dd}`;
  }
}

// Before & After Slider Interactivity
function initBeforeAfterSliders() {
  const sliders = document.querySelectorAll('.ba-slider-container');
  sliders.forEach(slider => {
    const before = slider.querySelector('.ba-before');
    const handle = slider.querySelector('.ba-slider-handle');
    let isDragging = false;

    function updateSlider(x) {
      const rect = slider.getBoundingClientRect();
      let pos = ((x - rect.left) / rect.width) * 100;
      pos = Math.max(2, Math.min(98, pos));
      before.style.clipPath = `inset(0 ${100 - pos}% 0 0)`;
      handle.style.left = pos + '%';
    }

    slider.addEventListener('mousedown', (e) => {
      isDragging = true;
      updateSlider(e.clientX);
      e.preventDefault();
    });

    window.addEventListener('mousemove', (e) => {
      if (isDragging) updateSlider(e.clientX);
    });

    window.addEventListener('mouseup', () => {
      isDragging = false;
    });

    // Touch support
    slider.addEventListener('touchstart', (e) => {
      isDragging = true;
      updateSlider(e.touches[0].clientX);
    }, { passive: true });

    slider.addEventListener('touchmove', (e) => {
      if (isDragging) updateSlider(e.touches[0].clientX);
    }, { passive: true });

    slider.addEventListener('touchend', () => {
      isDragging = false;
    });
  });
}

// Scroll-triggered progress bar animations
function initProgressBars() {
  const progressBars = document.querySelectorAll('.ba-progress-fill');
  if (!progressBars.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.animation = 'none';
        void entry.target.offsetWidth; // force reflow
        entry.target.style.animation = 'baProgressGrow 1.5s 0.3s forwards cubic-bezier(0.4, 0, 0.2, 1)';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  progressBars.forEach(bar => {
    bar.style.width = '0';
    bar.style.animation = 'none';
    observer.observe(bar);
  });
}

// Scroll-triggered stagger animations for cards
function initScrollAnimations() {
  const animatedCards = document.querySelectorAll('.ba-impact-card, .tech-feature-card');
  if (!animatedCards.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.animationPlayState = 'running';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.2 });

  animatedCards.forEach(card => {
    card.style.animationPlayState = 'paused';
    observer.observe(card);
  });
}

// Initialize all behaviours after DOM ready
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initDirection();
  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) themeToggle.addEventListener('click', toggleTheme);
  const rtlToggle = document.getElementById('rtl-toggle');
  if (rtlToggle) rtlToggle.addEventListener('click', toggleDirection);
  initMenu();
  initBackToTop();
  initLightbox();
  initPasswordToggles();
  initFormValidation();
  initBookingForm();
  initBeforeAfterSliders();
  initProgressBars();
  initScrollAnimations();
});