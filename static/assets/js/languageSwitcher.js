document.addEventListener('DOMContentLoaded', () => {
    const translateButton = document.getElementById('translate-button');
    const languageList = document.getElementById('language-list');
  
    translateButton.addEventListener('click', (event) => {
      event.stopPropagation(); 
      languageList.classList.toggle('visible'); 
    });
  
    document.addEventListener('click', (event) => {
      if (!translateButton.contains(event.target) && !languageList.contains(event.target)) {
        languageList.classList.remove('visible');
      }
    });
  });