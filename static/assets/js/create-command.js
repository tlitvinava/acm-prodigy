let command_buttons = document.querySelectorAll(".command-type a");
let univer_buttons = document.querySelectorAll(".univer-type a");

let command_input = document.querySelector("input[name='command_type']");
let univer_input = document.querySelector("input[name='univer_type']");

command_buttons.forEach((button) => {
    button.addEventListener("click", (event) => {
        event.preventDefault();

        document.querySelector(".command-type a.active").classList.remove("active");
        button.classList.add("active");
        command_input.value = button.dataset.key;
        console.log(command_input.value)
    });
});

univer_buttons.forEach((button) => {
    button.addEventListener("click", (event) => {
        event.preventDefault();

        document.querySelector(".univer-type a.active").classList.remove("active");
        button.classList.add("active");
        univer_input.value = button.dataset.key;
        console.log(univer_input.value)
    });
});
