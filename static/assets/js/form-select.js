document.querySelectorAll(".form-select").forEach((select) => {
    let default_value = select.dataset.default;
    let default_option = select.querySelector("option[value='']");

    default_option.setAttribute("disabled", "");
    default_option.innerText = default_value;
});