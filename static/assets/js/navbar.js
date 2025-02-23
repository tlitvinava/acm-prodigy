let navbar = document.querySelector(".nav");

document.querySelector(".nav-open-button").addEventListener("click", function() {
    navbar.classList.add("opened");
});

document.querySelector(".nav-close-button").addEventListener("click", function() {
    navbar.classList.remove("opened");
});