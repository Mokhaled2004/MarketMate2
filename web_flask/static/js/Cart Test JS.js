// Existing fruit and vegetable products list
const fruitVegetableProducts = [
    {
        id: 0,
        image: '../static/images/images/apple.png',
        title: 'apple',
        price: 2,
    },
    {
        id: 1,
        image: '../static/images/images/patato.png',
        title: 'potato',
        price: 8,
    },
    {
        id: 2,
        image: '../static/images/images/chili.png',
        title: 'chili',
        price: 4,
    },
    {
        id: 3,
        image: '../static/images/images/onion.png',
        title: 'onion',
        price: 20,
    },
    {
        id: 4,
        image: '../static/images/images/tamato.png',
        title: 'tomato',
        price: 20,
    }
];

// Adding meat products to the existing fruitVegetableProducts array
const meatProducts = [
    {
        id: 21,
        image: '../static/images/images/beef.jpg',
        title: 'beef',
        price: 10,
    },
    {
        id: 22,
        image: '../static/images/images/chicken.jpg',
        title: 'chicken',
        price: 8,
    },
    {
        id: 23,
        image: '../static/images/images/lamb.jpg',
        title: 'lamb',
        price: 15,
    },
    {
        id: 24,
        image: '../static/images/images/goat.jpg',
        title: 'goat',
        price: 15,
    }
];

// Adding meat products to the existing fruitVegetableProducts array
const bakeryProducts = [
    {
        id: 31,
        image: '../static/images/images/whitebread.jpg',
        title: 'whitebread',
        price: 10,
    },
    {
        id: 32,
        image: '../static/images/images/ryebread.jpg',
        title: 'Ryebread',
        price: 8,
    },
    {
        id: 33,
        image: '../static/images/images/sourdoughbread.jpg',
        title: 'Sourdoughbread',
        price: 15,
    },
    {
        id: 34,
        image: '../static/images/images/croissant.jpg',
        title: 'Croissant',
        price: 15,
    }
];

// Adding meat products to the existing fruitVegetableProducts array
const snacksProducts = [
    {
        id: 41,
        image: '../static/images/images/chips.jpg',
        title: 'Chips',
        price: 10,
    },
    {
        id: 42,
        image: '../static/images/images/pretzels.jpg',
        title: 'Pretzels',
        price: 8,
    },
    {
        id: 43,
        image: '../static/images/images/popcorn.jpg',
        title: 'Popcorn',
        price: 15,
    },
    {
        id: 44,
        image: '../static/images/images/crackers.jpg',
        title: 'Crackers',
        price: 15,
    }
];

// Merge fruitVegetableProducts and meatProducts into a single categories array
const categories = [...fruitVegetableProducts, ...meatProducts, ...bakeryProducts, ...snacksProducts];

let i = 0;

// Function to switch between displaying fruit/vegetable and meat products
function switchCategory(category) {
    if (category === 'fruitVegetableProducts') {
        document.getElementById('categoryTitle').textContent = 'Fruits & Vegetables';
    } else if (category === 'meatProducts') {
        document.getElementById('categoryTitle').textContent = 'Meat';
    }
    else if (category === 'bakeryProducts') {
        document.getElementById('categoryTitle').textContent = 'Bakery Products';
    }
    else if (category === 'snacksProducts') {
        document.getElementById('categoryTitle').textContent = 'SnacksProducts';
    }
    
    displayProducts(category);
}

// Initial display of products (default: fruit/vegetable products)
displayProducts('fruitVegetableProducts');

// Function to display products based on the selected category
function displayProducts(category) {
    let products;
    if (category === 'fruitVegetableProducts') {
        products = fruitVegetableProducts;
    } else if (category === 'meatProducts') {
        products = meatProducts;
    } else if (category === 'bakeryProducts') {
        products = bakeryProducts;
    } else if (category === 'snacksProducts') {
        products = snacksProducts;
    }else {
        products = [];
    }

    document.getElementById('root').innerHTML = products.map((item) => {
        var { image, title, price } = item;
        return (
            `<div class='box'>
                <div class='img-box'>
                    <img class='images' src=${image}></img>
                </div>
                <div class='bottom'>
                    <p>${title}</p>
                    <h2>$ ${price}.00</h2>
                    <button onclick='addtocart(${item.id})'>Add to cart</button>
                </div>
            </div>`
        );
    }).join('');
}
var cart = [];

function addtocart(id) {
    const selectedProducts = categories.find(item => item.id === id);
    const itemIndex = cart.findIndex(item => item.id === id);
    
    if (itemIndex > -1) {
        cart[itemIndex].quantity += 1;
    } else {
        cart.push({...selectedProducts, quantity: 1});
    }
    displaycart();
}

function delElement(a) {
    if (cart[a].quantity > 1) {
        cart[a].quantity -= 1;
    } else {
        cart.splice(a, 1);
    }
    displaycart();
}

function displaycart() {
    let j = 0, total = 0;
    document.getElementById("count").innerHTML = cart.length;
    if (cart.length == 0) {
        document.getElementById('cartItem').innerHTML = "Your cart is empty";
        document.getElementById("total").innerHTML = "$ " + 0 + ".00";
    } else {
        document.getElementById("cartItem").innerHTML = cart.map((items) => {
            var { image, title, price, quantity } = items;
            total = total + (price * quantity);
            document.getElementById("total").innerHTML = "$ " + total + ".00";
            return (
                `<div class='cart-item'>
                    <div class='row-img'>
                        <img class='rowimg' src=${image}>
                    </div>
                    <p style='font-size:12px;'>${title}</p>
                    <p style='font-size:12px;'>Quantity: ${quantity}</p>
                    <h2 style='font-size: 15px;'>$ ${price * quantity}.00</h2>
                    <i class='fa-solid fa-trash' onclick='delElement(${j++})'></i>
                </div>`
            );
        }).join('');
    }
}