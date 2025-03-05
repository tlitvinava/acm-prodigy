document.addEventListener('DOMContentLoaded', () => {
    const sidebarButton = document.getElementById('burger-button');
    const sidebarMenu = document.querySelector('.mobile-menu');
  
    sidebarButton.addEventListener('click', (event) => {
      event.stopPropagation(); 
      sidebarMenu.classList.toggle('open'); 
    });
  
    sidebarMenu.querySelectorAll('a.mobile-menu-button').forEach(link => {
      link.addEventListener('click', (event) => {
        sidebarMenu.classList.remove('open');
      });
    });
  
    document.addEventListener('click', (event) => {
      if (!sidebarButton.contains(event.target) && !sidebarMenu.contains(event.target)) {
        sidebarMenu.classList.remove('open'); 
      }
    });
  });