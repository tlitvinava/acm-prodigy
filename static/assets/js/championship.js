let texts = document.querySelectorAll(".final-text");

document.querySelectorAll(".championship-button").forEach((button) => {
    button.addEventListener("click", function(ev) {
        let button = ev.target;

        document.querySelector(".championship-button.active").classList.remove("active");
        button.classList.add("active");

        document.querySelector(".final-text.active").classList.remove("active");
        texts[button.dataset.key].classList.add("active");
    });
});
