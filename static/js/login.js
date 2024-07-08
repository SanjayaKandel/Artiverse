function allowOnlyOneCheckbox() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach((checkbox) => {
        checkbox.addEventListener('change', function() {
            checkboxes.forEach((cb) => {
                if (cb !== checkbox) {
                    cb.checked = false;
                }
            });
        });
    });
}

// Call the function on page load
document.addEventListener('DOMContentLoaded', allowOnlyOneCheckbox);
