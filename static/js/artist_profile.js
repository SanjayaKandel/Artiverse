document.addEventListener("DOMContentLoaded", function() {
    var modal = document.getElementById("imageModal");
    var img = document.getElementById("profilePic");
    var modalImg = document.getElementById("modalImage");
    var span = document.getElementsByClassName("close")[0];
    var body = document.body;

    if (img) {
        img.onclick = function() {
            modal.style.display = "block";
            modalImg.src = this.src;
            body.classList.add('modal-open'); 
        }
    }

    if (span) {
        span.onclick = function() {
            modal.style.display = "none";
            body.classList.remove('modal-open'); 
        }
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
            body.classList.remove('modal-open');
        }
    }
});
