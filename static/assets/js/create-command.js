let command_buttons = document.querySelectorAll(".command-type button");
let univer_buttons = document.querySelectorAll(".univer-type button");

let command_input = document.querySelector("input[name='command_type']");
let univer_input = document.querySelector("input[name='univer_type']");

command_buttons.forEach((button) => {
    button.addEventListener("click", (event) => {
        event.preventDefault();
        let btn = event.target;
        document.querySelector(".command-type button.active-form-button").classList.remove("active-form-button");
        btn.classList.add("active-form-button");
        command_input.value = btn.dataset.key;
        console.log(command_input)
        console.log(btn.dataset.key)
        console.log(command_input.value)
    });
});

univer_buttons.forEach((button) => {
    button.addEventListener("click", (event) => {
        event.preventDefault();
        let btn = event.target;
        document.querySelector(".univer-type button.active-form-button").classList.remove("active-form-button");
        btn.classList.add("active-form-button");
        univer_input.value = btn.dataset.key;
        console.log(univer_input)
        console.log(btn.dataset.key)
        console.log(univer_input.value)
    });
});