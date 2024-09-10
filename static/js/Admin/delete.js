document.addEventListener("DOMContentLoaded", function() {
    const deleteButtons = document.querySelectorAll(".delete-btn");
    const deleteModal = document.getElementById("delete-modal");
    const cancelDeleteBtn = document.querySelector(".delete-modal .cancel-btn");
    const closeModalBtn = document.querySelector(".delete-modal .close-btn");
    const deleteForm = document.getElementById("delete-form");

    deleteButtons.forEach(button => {
        button.addEventListener("click", function() {
            const artId = this.getAttribute("data-art-id");
            deleteForm.setAttribute("action", `/admin/delete_artwork/${artId}/`);
            deleteModal.classList.add("visible");
            document.body.classList.add("no-scroll");
        });
    });

    cancelDeleteBtn.addEventListener("click", function() {
        deleteModal.classList.remove("visible");
        document.body.classList.remove("no-scroll");
    });

    closeModalBtn.addEventListener("click", function() {
        deleteModal.classList.remove("visible");
        document.body.classList.remove("no-scroll");
    });

    // Optionally, you might want to close the modal on form submission
    deleteForm.addEventListener("submit", function() {
        deleteModal.classList.remove("visible");
        document.body.classList.remove("no-scroll");
    });
});

