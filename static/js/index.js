// index.js

// Get Started button
const startBtn = document.getElementById("startBtn");
if (startBtn) {
    startBtn.addEventListener("click", function () {
        window.location.href = "/summarize";
    });
}

// Optional: Card hover effect (extra smooth feel)
const cards = document.querySelectorAll(".card");
if (cards.length) {
    cards.forEach(card => {
        card.addEventListener("mouseenter", () => {
            card.style.transform = "scale(1.05)";
            card.style.transition = "0.3s";
        });

        card.addEventListener("mouseleave", () => {
            card.style.transform = "scale(1)";
        });
    });
}