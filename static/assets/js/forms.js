form = document.querySelectorAll("form")[0]
submit = form.getElementsByClassName("submit")[0]

submit.onclick = function(e) {
    e.preventDefault()
    form.submit()
}
