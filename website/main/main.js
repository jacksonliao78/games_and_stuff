document.querySelector(".changetext").addEventListener("mouseover", function(){
  document.querySelector(".first").style.backgroundImage = "url('wow.png')";
});

document.querySelector(".changetext").addEventListener("mouseleave", function(){
  document.querySelector(".first").style.backgroundImage = "url('wow2.png')"
});

document.querySelector(".rounded-box").addEventListener("mouseover", function(){
  document.querySelector(".boxp").style.color = "#8AAAE5"
  document.querySelector(".works").style.color = "white"
  document.querySelector(".boxp").style.fontSize = "2.5em"
});

document.querySelector(".rounded-box").addEventListener("mouseleave", function(){
  document.querySelector(".boxp").style.color = "white"
  document.querySelector(".works").style.color = "rgb(6, 142, 195)"
  document.querySelector(".boxp").style.fontSize = "2em"
});
