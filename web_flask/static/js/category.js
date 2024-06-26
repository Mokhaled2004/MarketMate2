const products = [
    { id: 0, image: '../static/images/images/apple.png', title: 'apple', price: 2 },
    { id: 1, image: '../static/images/images/patato.png', title: 'potato', price: 8 },
    { id: 2, image: '../static/images/images/chili.png', title: 'chili', price: 4 },
    { id: 3, image: '../static/images/images/onion.png', title: 'onion', price: 20 },
    { id: 4, image: '../static/images/images/tamato.png', title: 'tomato', price: 20 }
];

const categories = [...new Set(products.map(item => item))];
let cart = [];

function addToCart(index) {
    cart.push({ ...categories[index] });
    displayCart();
    updateCartCount();
}

function deleteElement(index) {
    cart.splice(index, 1);
    displayCart();
    updateCartCount();
}

function displayCart() {
    let total = 0;
    document.getElementById('cartItem').innerHTML = cart.length === 0
        ? "Your cart is empty"
        : cart.map((item, index) => {
            total += item.price;
            return `
                <div class='cart-item'>
                    <div class='row-img'>
                        <img class='rowimg' src='${item.image}' alt='${item.title}'>
                    </div>
                    <p style='font-size:12px;'>${item.title}</p>
                    <h2 style='font-size:15px;'>$ ${item.price}.00</h2>
                    <i class='fa-solid fa-trash' onclick='deleteElement(${index})'></i>
                </div>
            `;
        }).join('');
    document.getElementById('total').innerText = `$ ${total}.00`;
}

function updateCartCount() {
    document.querySelector('.right-nav .like span').innerText = cart.length;
}
