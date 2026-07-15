$(document).ready(function () {
    // document.querySelectorAll('.product-qty-box').forEach(box => {
    document.querySelectorAll('.product-qty-box, .pocket-product-qty').forEach(box => {
        const incrementBtn = box.querySelector('.increment');
        const decrementBtn = box.querySelector('.decrement');
        const qtyInput = box.querySelector('.cart_qty');

        incrementBtn.addEventListener('click', () => {
            console.log("Increment clicked");
            let currentValue = parseInt(qtyInput.value) || 0;
            const maxValue = parseInt(qtyInput.max) || 50;
            if (currentValue < maxValue) {
                qtyInput.value = currentValue + 1;
                updateCart(qtyInput);
            }
        });

        decrementBtn.addEventListener('click', () => {
            let currentValue = parseInt(qtyInput.value) || 0;
            const minValue = parseInt(qtyInput.min) || 0;
            if (currentValue > minValue) {
                qtyInput.value = currentValue - 1;
                updateCart(qtyInput);
            }
        });
    });

    $('#add_to_cart').on('click', function (e) {
        e.preventDefault();
        const parentRow = $(this).parent().parent();
        
        if (parentRow.length) {
            // const qtyInput = document.getElementById('cart_qty');
            const qtyInput = parentRow.find('#cart_qty');

            if (qtyInput.length) {
                let currentValue = parseInt(qtyInput.val()) || 0;
                if (currentValue === 0) {
                    // qtyInput.value = 1;
                    qtyInput.val(1);
                } else {
                    // qtyInput.value = 0;
                    qtyInput.val(0);
                }        
                updateCart(qtyInput);
            }
        }
    });

    document.querySelectorAll('button[id^="delete_cart__"]').forEach(deleteLink => {
        deleteLink.onclick = function (event) {
            event.preventDefault();
            const parentRow = this.closest('tr');
            // console.log(parentRow);

            if (parentRow) {
                // console.log('Parent Row:', parentRow);
                // parentRow.remove();

                const qtyInput = parentRow.querySelector('#cart_qty');

                let currentValue = parseInt(qtyInput.value) || 0;
                if (currentValue === 0) {
                    qtyInput.value = 1;
                } else {
                    qtyInput.value = 0;
                }        
                updateCart(qtyInput);
            }
        }; 
    });

    function updateCart(qtyInput) {
        const productId = $(qtyInput).data('product-id');
        const newQty = $(qtyInput).val();

        console.log("Product ID:", $(qtyInput).data("product-id"));
    console.log("Quantity:", $(qtyInput).val());
        // ajax diye korle page load hoina load charai update kore
        $.ajax({
            url: '/backend/add-or-update-cart/',
            type: 'POST',
            data: {
                'product_id': productId,
                'quantity': newQty,
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function (response) {




                console.log("Server Response:", response);


                if (!response.is_authenticated) {
                    const currentUrl = window.location.href;
                    const loginUrl = `/backend/login/?next=${encodeURIComponent(currentUrl)}`;
                    
                    window.location.href = loginUrl;
                    return;
                } else if (response.status === 'success') {
                    // Update Cart Quantity
                    var itemQuantityElements = document.getElementsByClassName('cart_qty__' + productId);
                    Array.from(itemQuantityElements).forEach(function (itemQuantityElement) {
                        itemQuantityElement.value = newQty;
                    });
                    // Update Cart Quantity
                    
                    // Update Cart Item
                    if (response.isRemoved) {
                        var cartItemElements = document.getElementsByClassName('cart_item__' + productId);
                        Array.from(cartItemElements).forEach(function (cartItemElement) {
                            cartItemElement.remove();
                        });
                    } else {
                        var itemPriceElements = document.getElementsByClassName('total_price__' + productId);
                        Array.from(itemPriceElements).forEach(function (itemPriceElement) {
                            itemPriceElement.innerHTML = `${response.item_price.toFixed(2)}`;
                        });
                    }
                    // Update Cart Item

                    var addButton = document.getElementById('add_to_cart');
                    if (addButton) {
                        if (newQty == 1 && addButton.innerHTML == 'Add to Cart') { location.reload(); }
                        
                        if (newQty > 0) { addButton.innerHTML = 'Remove from Cart'; }
                        else { addButton.innerHTML = 'Add to Cart'; }
                    }

                    // Update Cart Amounts
                    var subTotalAmountElements = document.getElementsByClassName('sub_total_amount');
                    Array.from(subTotalAmountElements).forEach(function (subTotalAmountElement) {
                        subTotalAmountElement.innerHTML = `${response.amount_summary.sub_total_amount.toFixed(2)}`;
                    });
                    // var subTotalAmount = document.getElementById('sub_total_amount');
                    // if (subTotalAmount) { subTotalAmount.innerHTML = `${response.amount_summary.sub_total_amount.toFixed(2)}`; }
                    
                    var vatAmount = document.getElementById('total_vat');
                    if (vatAmount) { vatAmount.innerHTML = `${response.amount_summary.total_vat.toFixed(2)}`; }
                    
                    var discountAmount = document.getElementById('total_discount');
                    if (discountAmount) { discountAmount.innerHTML = `${response.amount_summary.total_discount.toFixed(2)}`; }
                    
                    var grandTotalAmount = document.getElementById('grand_total');
                    if (grandTotalAmount) { grandTotalAmount.innerHTML = `${response.amount_summary.grand_total.toFixed(2)}`; }

                    
                    var cartItemCountElements = document.getElementsByClassName('cart_item_quantity');
                    Array.from(cartItemCountElements).forEach(function (cartItemCountElement) {
                        cartItemCountElement.innerHTML = response.cart_item_count;
                    });
                    // var cartItemCount = document.getElementById('cart_item_quantity');
                    // if (cartItemCount) {
                    //     // if (response.cart_item_count > 0) {
                    //         cartItemCount.innerHTML = response.cart_item_count;
                    //     //     cartItemCount.style.display = 'inline-block';
                    //     // } else {
                    //     //     cartItemCount.style.display = 'none';
                    //     // }
                    // }
                    // Update Cart Amounts
                } else {
                    alert('Failed to update the cart: ' + response.message);
                }
            },
            error: function (response) {
                console.error('Error updating cart:', response);
                if (!response.is_authenticated) {
                    const currentUrl = window.location.pathname;
                    const loginUrl = `/backend/login/?next=${encodeURIComponent(currentUrl)}`;
                    
                    window.location.href = loginUrl;
                    return;
                } else {
                    alert('An error occurred while updating the cart.');
                }
            }
        });
    }

    $('.cart_qty').on('change', function () {
        const productId = $(this).data('product-id');
        const newQty = $(this).val();
        updateCart(this);
    });

//hamburger-menu-show
const menuBtn = document.getElementById("menuBtn");
const mobileNav = document.getElementById("mobileNav");

if (menuBtn && mobileNav) {

    menuBtn.addEventListener("click", function () {

        mobileNav.classList.toggle("open");

        this.setAttribute(
            "aria-expanded",
            mobileNav.classList.contains("open")
        );

    });

    // Menu-এর বাইরে click করলে menu বন্ধ হবে
document.addEventListener("click", function (e) {

    if (
        !mobileNav.contains(e.target) &&
        !menuBtn.contains(e.target)
    ) {
        mobileNav.classList.remove("open");
    }

});

}
});