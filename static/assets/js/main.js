
document.addEventListener("DOMContentLoaded", () => {
    // Visual-only effects. No application/business logic is handled here.
    const revealItems = document.querySelectorAll(".reveal");
    revealItems.forEach((item, index) => {
        item.style.animationDelay = `${Math.min(index * 70, 500)}ms`;
    });

    const currentPath = window.location.pathname;
    document.querySelectorAll("[data-nav]").forEach(link => {
        if (link.getAttribute("href") === currentPath) {
            link.classList.add("active");
        }
    });
});
