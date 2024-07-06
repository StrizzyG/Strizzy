document.addEventListener("DOMContentLoaded", function() {
  const dropdownButton = document.querySelector('.dropdown-button');
  const dropdownContent = document.querySelector('.dropdown-content');

  dropdownButton.addEventListener('click', function() {
    dropdownContent.classList.toggle('open');
  });
});
