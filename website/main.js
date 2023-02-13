const prevBtn = document.querySelector('.prev-button');
const nextBtn = document.querySelector('.next-button');
const slider = document.querySelector('.slider');
const sliderImgs = Array.from(slider.children);
const time = 5000;
let activeSlide = 0;

//hide all images except the first one
sliderImgs.forEach((img, index) => {
  if (index !== 0) {
    img.style.display = 'none';
  }
});

//transition function
const transition = (sliderImgs, activeSlide, targetSlide) => {
  sliderImgs[activeSlide].classList.remove('active');
  sliderImgs[targetSlide].classList.add('active');
  sliderImgs[activeSlide].style.opacity = 0;
  sliderImgs[targetSlide].style.display = 'block';
  setTimeout(() => {
    sliderImgs[activeSlide].style.display = 'none';
    sliderImgs[targetSlide].style.opacity = 1;
  }, 1000);
}

//next button click
nextBtn.addEventListener('click', () => {
  activeSlide = (activeSlide + 1) % sliderImgs.length;
  transition(sliderImgs, activeSlide, (activeSlide + 1) % sliderImgs.length);
});

//previous button click
prevBtn.addEventListener('click', () => {
  activeSlide = (activeSlide - 1 + sliderImgs.length) % sliderImgs.length;
  transition(sliderImgs, activeSlide, (activeSlide - 1 + sliderImgs.length) % sliderImgs.length);
});
