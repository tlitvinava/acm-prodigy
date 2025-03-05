document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('nav button.step-button');
    const contents = document.querySelectorAll('.card-description');
  
    buttons.forEach(button => {
      button.addEventListener('click', function() {
        const targetId = this.getAttribute('data-target');
        const targetContent = document.querySelector(targetId);
  
        contents.forEach(content => content.classList.remove('active'));
  
        if (targetContent) {
          targetContent.classList.add('active');
        }
      });
    });
  
    contents[0].classList.add('active');
  });

  const buttons = document.querySelectorAll('.step-button');

  buttons.forEach(button => {
    button.addEventListener('click', () => {
      buttons.forEach(btn => btn.classList.remove('step-button-active'));
      button.classList.add('step-button-active');
    });
  });
  