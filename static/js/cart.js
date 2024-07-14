document.addEventListener('DOMContentLoaded', function () {
    // Function to show a popup notification
    function showAddedToCartPopup(itemName) {
        const popup = document.createElement('div');
        popup.classList.add('popup');
        popup.textContent = `${itemName} added to cart`;

        document.body.appendChild(popup);

        setTimeout(() => {
            popup.remove();
        }, 3000); // Remove the popup after 3 seconds
    }

    // Function to update item quantity and total price
    function updateItemQuantity(itemId, change) {
        const quantityElement = document.querySelector(`#quantity-update-${itemId}`);
        const quantitySpan = document.querySelector(`#quantity-${itemId}`);
        const totalPriceElement = document.querySelector(`#total-price-${itemId}`);
        const initialPriceElement = document.querySelector(`#initial-price-${itemId}`);

        // Get current quantity and price per item
        let currentQuantity = parseInt(quantityElement.textContent);
        const pricePerItem = parseFloat(initialPriceElement.textContent);

        // Update quantity
        currentQuantity += change;
        if (currentQuantity < 1) {
            currentQuantity = 1;
        }
        quantityElement.textContent = currentQuantity;
        quantitySpan.textContent = currentQuantity;

        // Calculate new total price
        const newTotalPrice = (currentQuantity * pricePerItem).toFixed(2);
        totalPriceElement.textContent = `Rs. ${newTotalPrice}`;

        // Update subtotal and total prices
        updatePrices();
    }

    // Function to update subtotal and total prices
    function updatePrices() {
        const subtotalElement = document.querySelector('#subtotal');
        const totalElement = document.querySelector('#total');
        const checkoutCountElement = document.querySelector('#checkout-count');
        const deleteButton = document.querySelector('.delete-btn');
        const itemCheckboxes = document.querySelectorAll('.item-checkbox:checked');
    
        let subtotal = 0;
    
        itemCheckboxes.forEach(checkbox => {
            const itemId = checkbox.getAttribute('data-item-id');
            const totalPriceElement = document.querySelector(`#total-price-${itemId}`);
            if (totalPriceElement) {
                const totalPrice = parseFloat(totalPriceElement.textContent.replace('Rs. ', ''));
                subtotal += totalPrice;
            }
        });
    
        if (subtotalElement) {
            subtotalElement.textContent = `Rs. ${subtotal.toFixed(2)}`;
        }
        if (totalElement) {
            totalElement.textContent = `Rs. ${subtotal.toFixed(2)}`;
        }
        if (checkoutCountElement) {
            checkoutCountElement.textContent = itemCheckboxes.length;
        }
    
        // Enable or disable delete button based on selection
        if (deleteButton) {
            deleteButton.disabled = itemCheckboxes.length === 0;
        }
    
        // Update SELECT ALL checkbox state
        const selectAllCheckbox = document.querySelector('#select-all');
        if (selectAllCheckbox) {
            selectAllCheckbox.checked = (itemCheckboxes.length === document.querySelectorAll('.item-checkbox').length);
        }
    }

    // Event listener for quantity buttons
    document.querySelectorAll('.quantity-btn').forEach(button => {
        button.addEventListener('click', function () {
            const itemId = this.getAttribute('data-item-id');
            const change = parseInt(this.getAttribute('data-change'));
            updateItemQuantity(itemId, change);
        });
    });

    // Event listener for SELECT ALL checkbox
    const selectAllCheckbox = document.querySelector('#select-all');
    if (selectAllCheckbox) {
        selectAllCheckbox.addEventListener('change', function () {
            const checkboxes = document.querySelectorAll('.item-checkbox');
            checkboxes.forEach(checkbox => {
                checkbox.checked = this.checked;
            });
            updatePrices();
        });
    }

    // Event listener for individual item checkboxes
    document.querySelectorAll('.item-checkbox').forEach(checkbox => {
        checkbox.addEventListener('change', function () {
            updatePrices();
        });
    });

    // Event listener for delete button
    const deleteButton = document.querySelector('.delete-btn');
    if (deleteButton) {
        deleteButton.addEventListener('click', function () {
            const itemCheckboxes = document.querySelectorAll('.item-checkbox:checked');
            itemCheckboxes.forEach(checkbox => {
                const itemId = checkbox.getAttribute('data-item-id');
                fetch(`/delete-item/${itemId}/`, {
                    method: 'DELETE',
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken')  // Ensure CSRF token is included
                    },
                })
                .then(response => {
                    if (response.ok) {
                        // Remove item from DOM on successful deletion
                        const listItem = checkbox.closest('.cart-item');
                        listItem.remove();
                        updatePrices();
                    } else {
                        console.error('Failed to delete item');
                    }
                })
                .catch(error => {
                    console.error('Error deleting item:', error);
                });
            });
        });
    }

    // Event listener for "Add to Cart" button
    const addToCartButton = document.querySelector('#add-to-cart');
    if (addToCartButton) {
        addToCartButton.addEventListener('click', function (event) {
            event.preventDefault(); // Prevent default anchor behavior
            const url = this.getAttribute('data-url');

            fetch(url, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({})
            })
            .then(response => response.json())
            .then(data => {
                showAddedToCartPopup(data.item_name);
                // Optionally update the cart count in the UI
                const cartCountElement = document.querySelector('#cart-item-count');
                if (cartCountElement) {
                    cartCountElement.textContent = data.cart_count;
                }
                // Redirect to cart view
                window.location.href = '/cart/'; // Update this URL if your cart view URL is different
                // window.location.href = '192.168.1.156/cart/';
            })
            .catch(error => {
                console.error('Error adding item to cart:', error);
            });
        });
    }

    // Function to get CSRF token from cookies (for CSRF protection in Django)
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Check if the cookie name matches the requested name
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Initial price calculation on page load
    updatePrices();
});
