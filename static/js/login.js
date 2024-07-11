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

document.addEventListener('DOMContentLoaded', allowOnlyOneCheckbox);
