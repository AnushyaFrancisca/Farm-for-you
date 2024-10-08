document.addEventListener("DOMContentLoaded", function () {
    const addNewBox = document.getElementById("add-new-box");
    const marketContainer = document.getElementById("market-container");
    const modal = document.getElementById("product-modal");
    const form = document.getElementById("product-form");
    const closeBtn = document.querySelector(".close-btn");
    const navToggle = document.getElementById("nav-toggle");

    let currentEditBox = null; // Track which box is being edited

    // Open modal on clicking add-new box
    addNewBox.addEventListener("click", () => {
        // Reset form for adding a new product
        currentEditBox = null; // Reset for new product
        modal.style.display = "flex";
        form.reset(); // Clear the form
    });

    // Close modal on clicking close button or outside modal
    closeBtn.addEventListener("click", () => {
        modal.style.display = "none";
    });

    window.onclick = (event) => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    };

    // Form submit handling
    form.addEventListener("submit", function (event) {
        event.preventDefault();

        // Retrieve input values
        const productName = document.getElementById("product-name").value;
        const productQuantity = document.getElementById("product-quantity").value;
        const productPrice = document.getElementById("product-price").value;
        const productImage = document.getElementById("product-image").files[0];

        // If editing an existing box
        if (currentEditBox) {
            const imgElement = currentEditBox.querySelector("img");
            const productDetails = currentEditBox.querySelector(".product-details");

            const reader = new FileReader();
            reader.onload = function (e) {
                imgElement.src = e.target.result; // Update image if provided
                productDetails.innerHTML = `
                    <img src="${e.target.result}" alt="Product Image">
                    <span><strong>Product  :</strong> ${productName}</span>
                    <span><strong>Quantity :</strong> ${productQuantity} kg</span>
                    <span><strong>Price    :</strong> ₹${productPrice}/half kg</span>
                `;
            };

            // If a new image is provided, read it, otherwise just update the details
            if (productImage) {
                reader.readAsDataURL(productImage);
            } else {
                productDetails.innerHTML = `
                    <img src="${imgElement.src}" alt="Product Image">
                    <span><strong>Product  :</strong> ${productName}</span>
                    <span><strong>Quantity :</strong> ${productQuantity} kg</span>
                    <span><strong>Price    :</strong> ₹${productPrice}/half kg</span>
                `;
            }

        } else { // Create a new product box
            const newBox = document.createElement("div");
            newBox.classList.add("product-box");

            const reader = new FileReader();
            reader.onload = function (e) {
                newBox.innerHTML = `
                    <div class="product-details">
                        <img src="${e.target.result}" alt="Product Image">
                        <span><strong>Product  :</strong> ${productName}</span>
                        <span><strong>Quantity :</strong> ${productQuantity} kg</span>
                        <span><strong>Price    :</strong> ₹${productPrice}/half kg</span>
                    </div>
                    <div class="edit-delete-buttons">
                        <button class="edit-btn">Edit</button>
                        <button class="delete-btn">Delete</button>
                    </div>
                `;

                // Insert new product box before add-new box
                marketContainer.insertBefore(newBox, addNewBox);

                // Handle delete button
                const deleteBtn = newBox.querySelector(".delete-btn");
                deleteBtn.addEventListener("click", function () {
                    newBox.remove();
                });

                // Handle edit button
                const editBtn = newBox.querySelector(".edit-btn");
                editBtn.addEventListener("click", function () {
                    currentEditBox = newBox; // Track the box being edited
                    document.getElementById("product-name").value = productName; // Pre-fill name
                    document.getElementById("product-quantity").value = productQuantity; // Pre-fill quantity
                    document.getElementById("product-price").value = productPrice; // Pre-fill price
                    modal.style.display = "flex"; // Open modal
                });
            };
            reader.readAsDataURL(productImage);
        }

        // Reset form and hide modal
        form.reset();
        modal.style.display = "none";
    });

    // Handle navbar toggle event to adjust margin and layout
    navToggle.addEventListener("change", function () {
        if (navToggle.checked) {
            marketContainer.classList.add("expanded");
        } else {
            marketContainer.classList.remove("expanded");
        }
    });
});
