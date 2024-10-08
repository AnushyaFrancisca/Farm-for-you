// logout.js
document.addEventListener("DOMContentLoaded", function() {
    const modal = document.getElementById("logout-modall");
    const logoutButton = document.querySelector(".fa-power-off").parentElement;
    const yesButton = document.getElementById("yes-buttonn");
    const noButton = document.getElementById("no-buttonn");

    // Show modal on clicking logout
    logoutButton.addEventListener("click", function() {
      modal.style.display = "flex";
    });

    // Close modal on clicking 'No' button
    noButton.addEventListener("click", function() {
      modal.style.display = "none";
    });

    // Action for 'Yes' button (e.g., redirect to logout URL)
    yesButton.addEventListener("click", function() {
      window.location.href = "/logout"; // Adjust to your actual logout URL
    });

    // Close the modal when clicking outside the modal content
    window.addEventListener("click", function(event) {
      if (event.target === modal) {
        modal.style.display = "none";
      }
    });
});