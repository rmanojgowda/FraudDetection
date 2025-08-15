// Dynamic Product Details
if (document.location.href.includes('product.html')) {
    const params = new URLSearchParams(window.location.search);
    const product = params.get('product');

    const productName = document.getElementById('product-name');
    const price = document.getElementById('price');
    const productImage = document.getElementById('product-image');

    if (product === '1') {
        productName.innerText = 'Product 1';
        price.innerText = '$100';
        productImage.src = 'product1.jpg';
    } else if (product === '2') {
        productName.innerText = 'Product 2';
        price.innerText = '$200';
        productImage.src = 'product2.jpg';
    }
}

function redirectToPayment() {
    const price = document.getElementById('price').innerText;
    window.location.href = `payment.html?price=${encodeURIComponent(price)}`;
}

// Payment Page Logic
if (document.location.href.includes('payment.html')) {
    const params = new URLSearchParams(window.location.search);
    const shownPrice = params.get('price');

    const shownPriceElement = document.getElementById('shown-price');
    const deductedPriceElement = document.getElementById('deducted-price');

    shownPriceElement.innerText = shownPrice || '$0';
    deductedPriceElement.innerText = shownPrice
        ? `$${parseInt(shownPrice.slice(1)) + 50}` // Fraudulent addition
        : '$0';
}

function redirectToBlank() {
    alert('Payment processed successfully! Redirecting...');
    window.location.href = 'blank.html';
}
// Placeholder for future functionality
document.addEventListener('DOMContentLoaded', () => {
    console.log('Amazon Clone Ready!');
    
    // Search functionality (placeholder)
    document.querySelector('.search-bar button').addEventListener('click', () => {
        alert('Search functionality coming soon!');
    });
});
