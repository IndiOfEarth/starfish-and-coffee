// How navSlide animation works
// 1. function looks for the necessary elements using document.querySelector
// 2. On the burger element, we create an EventListener that waits for a click
// 3. When clicked, We add the class 'nav-toggle' to the nav element and 'toggle' to the burger element
// 4. For each link in the navlinks array, play the CSS animation if it hasn't been started already

const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    burger.addEventListener('click', ()=> {
        nav.classList.toggle('nav-active'); // toggle nav
        burger.classList.toggle('toggle'); //burger animation

        // animate the links
        // creates a nice delay between each link, using index
        navLinks.forEach((link,index)=>{
            if(link.style.animation) {
                link.style.animation = '';
            }
            else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.5}s`;
            }
        });
    });

}

function zoom() {
    document.body.style.zoom = "90%"
}


// if website scroll is at the top
    // navbar backgroundcolor = white
// else
    // navbar backgroundColor = brown
const navbar = document.querySelector('.navbar');
window.addEventListener('scroll', () => {
    const scrolled = window.scrollY;

    // if website hasn't scrolled, then remove .scrolled class
    if (scrolled === 0) {
        navbar.classList.remove('scrolled');
    }
    // but if scrolled, add .scrolled class
    else {
        navbar.classList.add('scrolled');
    }

});



// Get the modal, button, span (that closes modal)
var modal = document.getElementById("editModal")
var btn = document.querySelector(".edit-button");
var span = document.querySelector(".close");

// when user clicks button, open the modal
btn.onclick = function() {
    modal.style.display = "block";
}

// when user clicks span, close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// when user clicks anywhere outside of modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}



zoom();
navSlide();
