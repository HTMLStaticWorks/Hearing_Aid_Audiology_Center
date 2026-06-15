// assets/js/main.js – Handles theme, RTL, menu, and back‑to‑top
// <link href="assets/css/dark-mode.css" rel="stylesheet" id="dark-mode-stylesheet" disabled>
// <link href="assets/css/rtl.css" rel="stylesheet" id="rtl-stylesheet" disabled> back‑to‑top

// Utility to set data attribute and persist in localStorage
function setTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('theme', theme);
  document.getElementById('theme-toggle').textContent = theme === 'dark' ? '☀️' : '🌙';
  // Enable/disable dark‑mode stylesheet
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
  document.getElementById('rtl-toggle').textContent = dir === 'rtl' ? 'LTR' : 'RTL';
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

// Off‑canvas menu for small screens
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

// Back‑to‑top button
function initBackToTop() {
  const btn = document.getElementById('back-to-top');
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
});
