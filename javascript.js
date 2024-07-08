// Smooth scroll effect for internal links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();

    const target = document.querySelector(this.getAttribute('href'));
    target.scrollIntoView({
      behavior: 'smooth'
    });
  });
});

// Fade-in effect for sections on scroll
const sections = document.querySelectorAll('.fade-in');
const options = {
  root: null,
  rootMargin: '0px',
  threshold: 0.3
};

const observer = new IntersectionObserver(function(entries, observer) {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, options);

sections.forEach(section => {
  observer.observe(section);
});
