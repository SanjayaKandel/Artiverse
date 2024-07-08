function showSection(sectionId) {
    const sections = document.querySelectorAll('.popup-section');
    sections.forEach(section => section.style.display = 'none');
    document.getElementById(sectionId).style.display = 'block';
}
document.addEventListener('DOMContentLoaded', function() {
    // Your existing JavaScript code here
    document.querySelector('.profile-dropdown-list-item a[href="#"]').addEventListener('click', function(e) {
        e.preventDefault();
        showSection('profile-details-section');
    });

    document.querySelector('.profile-dropdown-list-item a[href="#favorites"]').addEventListener('click', function(e) {
        e.preventDefault();
        showSection('favorites-section');
    });

    document.querySelector('.profile-dropdown-list-item a[href="#order-history"]').addEventListener('click', function(e) {
        e.preventDefault();
        showSection('order-history-section');
    });

    document.querySelector('.profile-dropdown-list-item a[href="#settings"]').addEventListener('click', function(e) {
        e.preventDefault();
        showSection('settings-section');
    });

    function showSection(sectionId) {
        const sections = document.querySelectorAll('.popup-section');
        sections.forEach(section => section.style.display = 'none');
        document.getElementById(sectionId).style.display = 'block';
    }
});
