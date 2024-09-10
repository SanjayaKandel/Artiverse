document.addEventListener("DOMContentLoaded", function() {
    const deleteButtons = document.querySelectorAll(".delete-btn");
    const deleteModal = document.getElementById("delete-modal");
    const cancelDeleteBtn = document.querySelector("#delete-modal .cancel-btn");
    const closeModalBtn = document.querySelector("#delete-modal .close-btn");
    const deleteForm = document.getElementById("delete-form");

    deleteButtons.forEach(button => {
        button.addEventListener("click", function(event) {
            event.preventDefault();  // Prevent default behavior of button click
            const userId = this.getAttribute("data-user-id");
            deleteForm.setAttribute("action", `/admin/delete/artist/${userId}/`);
            deleteModal.classList.add("visible");
            document.body.classList.add("no-scroll");
        });
    });

    cancelDeleteBtn.addEventListener("click", function(event) {
        event.preventDefault();
        deleteModal.classList.remove("visible");
        document.body.classList.remove("no-scroll");
    });

    closeModalBtn.addEventListener("click", function(event) {
        event.preventDefault();
        deleteModal.classList.remove("visible");
        document.body.classList.remove("no-scroll");
    });

    deleteForm.addEventListener("submit", function(event) {
        deleteModal.classList.remove("visible");
        document.body.classList.remove("no-scroll");
    });
});
