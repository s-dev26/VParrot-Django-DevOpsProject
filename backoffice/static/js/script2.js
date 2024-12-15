const navbar = document.querySelector(".header_ .navbar");
const menuButton = document.querySelector(".header_ .menu");
menuButton.addEventListener("click", () => {
  navbar.classList.toggle("show");
  menuButton.classList.toggle("fa-close");
});
