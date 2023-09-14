//open modal
document.getElementById("button-open-modal").addEventListener("click", function() {
    document.getElementById("my-modal").classList.add("open");
    document.getElementById("body").classList.add("lock");
});

//close modal
document.getElementById("button-close-modal").addEventListener("click", function() {
    document.getElementById("my-modal").classList.remove("open");
    document.getElementById("body").classList.remove("lock");
});

//close enter esc
window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
        document.getElementById("my-modal").classList.remove("open")
        document.getElementById("body").classList.remove("lock");
    }
});

//
document.querySelector("#my-modal .modal-box").addEventListener('click', event => {
    event._isClickWithInModal = true;
});
document.getElementById("my-modal").addEventListener('click', event => {
    if (event._isClickWithInModal) return;
    event.currentTarget.classList.remove('open');
    document.getElementById("body").classList.remove("lock");
});