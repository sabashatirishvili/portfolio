document.addEventListener('DOMContentLoaded', () => {
  const buttons = document.querySelectorAll('.category div');
  const technologiesContainer = document.querySelector('.skill-list');

  buttons.forEach(button => {
    button.addEventListener('click', async () => {
      category = button.getAttribute('data-category');
      try {
        const response = await fetch(`/technologies/${category}`);
        const data = await response.json();
        const technologiesHTML = data.map(tech => `<div>${tech.name}</div>`).join('');
        technologiesContainer.innerHTML = technologiesHTML;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    })
  })
})