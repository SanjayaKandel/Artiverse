document.addEventListener("DOMContentLoaded", function() {
    const deleteButtons = document.querySelectorAll(".delete-btn");
    const deleteModal = document.getElementById("delete-modal");
    const cancelDeleteBtn = document.querySelector(".delete-modal .cancel-btn");
    const closeModalBtn = document.querySelector(".delete-modal .close-btn");
    const deleteForm = document.getElementById("delete-form");

    deleteButtons.forEach(button => {
        button.addEventListener("click", function() {
            const artId = this.getAttribute("data-art-id");
            deleteForm.setAttribute("action", `/Artwork/delete/${artId}/`);
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


// See more
$(document).ready(function() {
    $('.see-more').click(function(event) {
        event.preventDefault(); 

        var $description = $(this).closest('.artwork-info').find('.description');
        
        if ($description.hasClass('expanded')) {
            // Collapse the description
            $description.removeClass('expanded');
            $description.css('max-height', '100px'); 
            $(this).text('See More'); // Change button text to "See More"
        } else {
            // Expand the description
            $description.addClass('expanded');
            $description.css('max-height', '100px'); 
            $(this).text('See Less'); // Change button text to "See Less"
        }
    });
});
