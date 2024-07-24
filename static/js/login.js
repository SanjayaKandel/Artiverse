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
    const usernameField = document.querySelector('#id_username');
    const passwordField = document.querySelector('#id_password');
    
    if (usernameField) {
        usernameField.setAttribute('placeholder', '\uf007 Username'); // User icon
        usernameField.classList.add('placeholder-icon-username');
    }
    
    if (passwordField) {
        passwordField.setAttribute('placeholder', '\uf023 Password'); // Lock icon
        passwordField.classList.add('placeholder-icon-password');
    }

    // Show password
    const togglePassword = document.querySelector('#toggle-password');

    togglePassword.addEventListener('click', function() {
        const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordField.setAttribute('type', type);
        this.classList.toggle('fa-eye');
        this.classList.toggle('fa-eye-slash');
    });
});