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

    // Form submit handling for adding a new product
    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const formData = new FormData(form);
        const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

        fetch("{% url 'market_view' %}", {
            method: "POST",
            headers: {
                "X-CSRFToken": csrfToken,
            },
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                console.log("Product successfully added to the database");

                const newBox = document.createElement("div");
                newBox.classList.add("product-box");

                const reader = new FileReader();
                const productImage = document.getElementById("product-image").files[0];

                reader.onload = function (e) {
                    newBox.innerHTML = `
                        <div class="product-details">
                            <img src="${e.target.result}" alt="Product Image">
                            <span><strong>Product:</strong> ${document.getElementById("product-name").value}</span>
                            <span><strong>Quantity:</strong> ${document.getElementById("product-quantity").value} kg</span>
                            <span><strong>Price:</strong> ₹${document.getElementById("product-price").value}/half kg</span>
                        </div>
                        <div class="edit-delete-buttons">
                            <button class="edit-btn">Edit</button>
                            <button class="delete-btn" data-product-id="${data.product_id}">Delete</button>
                        </div>
                    `;

                    marketContainer.insertBefore(newBox, addNewBox);
                };

                if (productImage) {
                    reader.readAsDataURL(productImage);
                }
            } else {
                console.error("Failed to add product:", data.message);
            }
        })
        .catch(error => {
            console.error("Error during form submission:", error);
        });

        // Reset form and hide modal
        form.reset();
        modal.style.display = "none";
    });

    function confirmDelete(productId) {
        const confirmAction = confirm("Are you sure you want to delete this product?");
        if (confirmAction) {
            // Proceed with the deletion if confirmed
            fetch(`/market/delete/${productId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.getElementById('csrf-token').value // Set CSRF token
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    alert('Product deleted successfully');
                    location.reload(); // Reload the page to reflect changes
                } else {
                    alert(data.message);
                }
            })
            .catch(error => {
                console.error('Error during delete operation:', error);
            });
        }
    }

    function showDeleteConfirmation(productId) {
        document.getElementById('delete-confirmation-modal').style.display = 'block'; // Show the modal
        // You can store the product ID here for deletion
    }    

// Edit button event listener
document.querySelectorAll('.edit-btn').forEach(button => {
    button.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the default action
        const productBox = this.closest('.product-box'); // Get the closest product box
        const productId = productBox.querySelector('.delete-btn').getAttribute('data-product-id'); // Get the product ID
        const productName = productBox.querySelector('span:nth-of-type(1)').textContent.split(': ')[1].trim();
        const productQuantity = productBox.querySelector('span:nth-of-type(2)').textContent.split(': ')[1].trim();
        const productPrice = productBox.querySelector('span:nth-of-type(3)').textContent.split('₹')[1].split('/')[0].trim();

        // Set the product ID to be edited
        productIdToDelete = productId;  // This should be the same variable used for deletion
        // Open the edit modal with the product data
        openEditModal({
            id: productId,
            name: productName,
            quantity: productQuantity,
            price: productPrice
        });
    });
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



// // market.js

// document.addEventListener('DOMContentLoaded', () => {
//     // Open the modal to add a new product
//     document.getElementById('add-new-box').addEventListener('click', () => {
//         document.getElementById('product-modal').style.display = 'block';
//     });

//     // Close the modal
//     document.querySelector('.close-btn').addEventListener('click', () => {
//         document.getElementById('product-modal').style.display = 'none';
//     });

//     // Add product form submission
//     document.getElementById('product-form').addEventListener('submit', (e) => {
//         e.preventDefault();
//         const formData = new FormData(e.target);
//         const url = document.getElementById('market-view-url').value;

//         fetch(url, {
//             method: 'POST',
//             body: formData,
//             headers: {
//                 'X-CSRFToken': document.getElementById('csrf-token').value
//             }
//         })
//         .then(response => response.json())
//         .then(data => {
//             if (data.status === 'success') {
//                 // Add the new product to the UI (you might want to fetch and refresh the product list)
//                 location.reload(); // Refresh the page to see the changes
//             } else {
//                 alert(data.message);
//             }
//         });
//     });

//     // Edit and Delete functionality
//     document.querySelectorAll('.edit-btn').forEach(button => {
//         button.addEventListener('click', (e) => {
//             const productBox = e.target.closest('.product-box');
//             const productId = productBox.getAttribute('data-id');
//             const productName = productBox.querySelector('span:nth-child(2)').textContent.split(': ')[1];
//             const productQuantity = productBox.querySelector('span:nth-child(3)').textContent.split(': ')[1].split(' ')[0];
//             const productPrice = productBox.querySelector('span:nth-child(4)').textContent.split(': ')[1].split('/')[0].trim().slice(1);

//             document.getElementById('product-name').value = productName;
//             document.getElementById('product-quantity').value = productQuantity;
//             document.getElementById('product-price').value = productPrice;
//             document.getElementById('product-modal').setAttribute('data-id', productId); // Store the product ID for editing
//             document.getElementById('product-modal').style.display = 'block';
//         });
//     });

//     document.querySelectorAll('.delete-btn').forEach(button => {
//         button.addEventListener('click', (e) => {
//             const productBox = e.target.closest('.product-box');
//             const productId = productBox.getAttribute('data-id');
    
//             if (confirm('Are you sure you want to delete this product?')) {
//                 fetch(`/delete_product/${productId}/`, {
//                     method: 'DELETE',
//                     headers: {
//                         'X-CSRFToken': document.getElementById('csrf-token').value
//                     }
//                 })
//                 .then(response => response.json())
//                 .then(data => {
//                     if (data.status === 'success') {
//                         productBox.remove(); // Remove the product from the UI
//                     } else {
//                         alert(data.message);
//                     }
//                 })
//                 .catch(error => {
//                     console.error('Error:', error);
//                 });
//             }
//         });
//     });
    
//     // Handle the update functionality
//     document.getElementById('product-form').addEventListener('submit', (e) => {
//         e.preventDefault();
//         const formData = new FormData(e.target);
//         const productId = document.getElementById('product-modal').getAttribute('data-id');
//         const url = `/update_product/${productId}/`;

//         fetch(url, {
//             method: 'POST',
//             body: formData,
//             headers: {
//                 'X-CSRFToken': document.getElementById('csrf-token').value
//             }
//         })
//         .then(response => response.json())
//         .then(data => {
//             if (data.status === 'success') {
//                 // Refresh the product list to reflect the changes
//                 location.reload(); // Refresh the page to see the changes
//             } else {
//                 alert(data.message);
//             }
//         });
//     });
// });
