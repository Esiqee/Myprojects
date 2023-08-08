const nameInput = document.getElementById('name-input');
const submitBtn = document.getElementById('submit-name');
const greeting = document.getElementById('greeting');
const userName = document.getElementById('user-name');
const introText = document.getElementById('intro-text');
const nextPageBtn = document.getElementById('next-page-btn');

submitBtn.addEventListener('click', () => {
  const name = nameInput.value;
  if (name) {
    userName.textContent = name;
    greeting.style.opacity = 1;
    introText.style.opacity = 1;
    nextPageBtn.style.opacity = 1;

  }
});
