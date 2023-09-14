//open modal
document.getElementById("button-open-modal").addEventListener("click", function() {
    document.getElementById("my-modal").classList.add("open")
})

//close modal
document.getElementById("button-close-modal").addEventListener("click", function() {
    document.getElementById("my-modal").classList.remove("open")
})