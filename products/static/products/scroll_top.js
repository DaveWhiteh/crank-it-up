// Products Page - Scroll to top functionality
// Modified from Code Institute's Boutique Ado Walkthrough

let button = document.getElementById("btt-button");

window.onscroll = function() {
    scrollFunction();
};

button.addEventListener('click', function(e) {
    document.body.scrollTop = document.documentElement.scrollTop = 0; // Cross-browser compatibility
});

function scrollFunction() {
    if (document.documentElement.scrollTop > 360) {
        button.style.display = "block";
    } else {
        button.style.display = "none";
    }
}