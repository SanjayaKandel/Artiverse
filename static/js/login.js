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

document.addEventListener('DOMContentLoaded', function() {
    const usernameField = document.querySelector('.placeholder-icon-username');
    const passwordField = document.querySelector('.placeholder-icon-password');
    
    if (usernameField) {
        usernameField.setAttribute('placeholder', '\uf007 Username'); // User icon
    }
    
    if (passwordField) {
        passwordField.setAttribute('placeholder', '\uf023 Password'); // Lock icon
    }

    
});

// Show password
document.addEventListener('DOMContentLoaded', function() {
    const togglePassword = document.querySelector('#toggle-password');
    const passwordField = document.querySelector('#id_password');

    togglePassword.addEventListener('click', function() {
        const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordField.setAttribute('type', type);
        this.classList.toggle('fa-eye');
        this.classList.toggle('fa-eye-slash');
    });
});