// Header Background Change on scroll
let navbar = document.querySelector("navbar");
window.addEventListener("scroll", () => {
    header.classList.toggle("shadow", window.scrollY > 0);
});