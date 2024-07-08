let profileDropdownList = document.querySelector(".profile-dropdown-list");
let btn = document.querySelector(".profile-dropdown-btn");

let classList = profileDropdownList.classList;

const toggle = () => classList.toggle("active");

window.addEventListener("click", function (e) {
    if (!btn.contains(e.target)) classList.remove("active");
});

// Toggle menu function for the hamburger menu
function toggleMenu() {
    const menuLinks = document.getElementById("menu-links");
    menuLinks.classList.toggle("active");

    if (menuLinks.classList.contains("active")) {
        document.addEventListener("click", handleClickOutside, true);
    } else {
        document.removeEventListener("click", handleClickOutside, true);
    }
}

function handleClickOutside(event) {
    const menuLinks = document.getElementById("menu-links");
    if (!menuLinks.contains(event.target) && !event.target.matches('button')) {
        menuLinks.classList.remove("active");
        document.removeEventListener("click", handleClickOutside, true);
    }
}
