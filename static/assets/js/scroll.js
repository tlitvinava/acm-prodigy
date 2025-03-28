function debounce(func, wait) {
    let timeout;
    return function(...args) {
      clearTimeout(timeout);
      timeout = setTimeout(() => func.apply(this, args), wait);
    };
  }
  
  document.addEventListener('DOMContentLoaded', () => {
    const navButtons = document.querySelectorAll('.menu .button');
    const homeButton = document.querySelector('.menu .button[data-target="#main-section"]');
  
    navButtons.forEach(button => button.classList.remove('active'));
  
    if (homeButton) {
      homeButton.classList.add('active');
    }
  });
  
  document.querySelectorAll('.menu .button').forEach(button => {
    button.addEventListener('click', function() {
      const targetId = this.getAttribute('data-target');
      const targetSection = document.querySelector(targetId);
  
      if (targetSection) {
        targetSection.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });

  window.addEventListener('scroll', debounce(() => {
    const sections = document.querySelectorAll('section');
    const navButtons = document.querySelectorAll('.menu .button');
  
    let closestSection = null;
    let closestDistance = Infinity;
  
    sections.forEach((section, index) => {
      const rect = section.getBoundingClientRect();
      const distance = Math.abs(rect.top); 
  
      if (distance < closestDistance && rect.top <= 170 && rect.bottom >= 130) {
        closestDistance = distance;
        closestSection = index;
      }
    });
  
    navButtons.forEach(button => button.classList.remove('active'));
    if (closestSection !== null) {
      navButtons[closestSection].classList.add('active');
    }
  }, 20));