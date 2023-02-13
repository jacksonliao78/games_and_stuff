const images = document.querySelectorAll(".slider img");
let currentImage = 0;

images[currentImage].classList.add("active");

const prevButton = document.querySelector(".prev-button");
const nextButton = document.querySelector(".next-button");

prevButton.addEventListener("click", () => {
  images[currentImage].classList.remove("active");
  currentImage = (currentImage - 1 + images.length) % images.length;
  images[currentImage].classList.add("active");
});

nextButton.addEventListener("click", () => {
  images[currentImage].classList.remove("active");
  currentImage = (currentImage + 1) % images.length;
  images[currentImage].classList.add("active");
});
