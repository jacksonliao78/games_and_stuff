let blob = document.getElementById('blob');

const onMouseMove = (e) =>{
  blob.animate({
    left: e.pageX + 'px',
    top: e.pageY + 'px'
  }, { duration: 3000, fill: "forwards"});
  
}
document.addEventListener('mousemove', onMouseMove);

