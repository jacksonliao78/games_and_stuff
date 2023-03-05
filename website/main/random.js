let blob = document.getElementById('blob');

const onMouseMove = (e) =>{
  blob.animate({
    left: e.pageX + 'px',
    top: e.pageY + 'px'
  }, { duration: 3000, fill: "forwards"});
  
}
document.addEventListener('mousemove', onMouseMove);

const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?";

let interval = null;

document.querySelector("h1").onmouseover = event => {  
  let iteration = 0;
  
  clearInterval(interval);
  
  interval = setInterval(() => {
    event.target.innerText = event.target.innerText
      .split("")
      .map((letter, index) => {
        if(index < iteration) {
          return event.target.dataset.value[index];
        }
      
        return letters[Math.floor(Math.random() * 64)]
      })
      .join("");
    
    if(iteration >= event.target.dataset.value.length){ 
      clearInterval(interval);
    }
    
    iteration += 1 / 3;
  }, 20);
}

const target = document.getElementById("target");
const textchange = document.getElementById("textchange");
const body = document.body;
const target2 = document.getElementById("text-box2");
const blurb = document.getElementById("blur");
const header = document.querySelector("header");

target.addEventListener("mouseover", () => {
  textchange.style.color = '#FFFFF7';
  body.style.background = 'black';
});

target.addEventListener("mouseleave", () => {
  textchange.style.color = 'transparent';
  body.style.background = 'black';
  header.classList.add('visible');
});

target2.addEventListener("mouseover", () => {
  blob.style.height = '8em';
  blurb.style.backdropFilter = 'blur(100px)';
});

target2.addEventListener("mouseleave", () => {
  blob.style.height = '12em';
  blurb.style.backdropFilter = 'blur(125px)';
});