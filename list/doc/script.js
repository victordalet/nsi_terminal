
/***********************************************/

const images = document.querySelectorAll(".code")
let options = {
  // root: null,
  rootMargin: "-10% 0px",
  threshold: 0.4
}

function handleIntersect(entries){
  console.log(entries);
  entries.forEach(entry => {
    if(entry.isIntersecting){
      entry.target.style.opacity = 1;
    }
  })
}

const observer = new IntersectionObserver(handleIntersect, options)

images.forEach(image => {
  observer.observe(image)
})


/********************************/


const loader = document.querySelector('.loader');

window.addEventListener('load',()=> {
  loader.classList.add('fondu-out');
})