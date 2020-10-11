let modal = document.getElementById("login-modal");
const formUrl = "SomeUrl"

function openModal(type) {
    let label = document.querySelector("#login-modal #exampleModalLabel");
    label.innerText = "Welcome " + type;
    link = formUrl + "/" + type.toLowerCase();
    document.getElementById("loginForm").setAttribute('action', link);
    $("#login-modal").modal('show');
}