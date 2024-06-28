// Existing fruit and vegetable products list
const fruitVegetableProducts = [
    {
        id: 0,
        image: '../static/images/images/apple.png',
        title: 'Apple',
        price: 30,
        quantity: 1
    },
    {
        id: 1,
        image: '../static/images/images/patato.png',
        title: 'Potato',
        price: 25,
        quantity: 1
    },
    {
        id: 2,
        image: '../static/images/images/chili.png',
        title: 'Chili',
        price: 20,
        quantity: 1
    },
    {
        id: 3,
        image: '../static/images/images/onion.png',
        title: 'Onion',
        price: 35,
        quantity: 1
    },
    {
        id: 4,
        image: '../static/images/images/tamato.png',
        title: 'Tomato',
        price: 35,
        quantity: 1
    },
    {
        id: 5,
        image: '../static/images/images/Oranges.jpg',
        title: 'Oranges',
        price: 40,
        quantity: 1
    },
    {
        id: 6,
        image: '../static/images/images/carrot.jpg',
        title: 'Carrot',
        price: 20,
        quantity: 1
    },
    {
        id: 7,
        image: '../static/images/images/broccoli.jpg',
        title: 'Broccoli',
        price: 45,
        quantity: 1
    },
    {
        id: 8,
        image: '../static/images/images/cucumber.jpg',
        title: 'Cucumber',
        price: 25,
        quantity: 1
    },
    {
        id: 9,
        image: '../static/images/images/Eggplant.jpg',
        title: 'Eggplant',
        price: 35,
        quantity: 1
    },
    {
        id: 10,
        image: '../static/images/images/strawberry.jpg',
        title: 'Strawberry',
        price: 40,
        quantity: 1
    },
    {
        id: 11,
        image: '../static/images/images/mango.jpg',
        title: 'Mango',
        price: 50,
        quantity: 1
    },
    {
        id: 12,
        image: '../static/images/images/cucumber.jpg',
        title: 'Cucumber',
        price: 25,
        quantity: 1
    },
    {
        id: 13,
        image: '../static/images/images/melon.jpg',
        title: 'Watermelon',
        price: 55,
        quantity: 1
    }
];
// Adding meat products to the existing fruitVegetableProducts array
const meatProducts = [
    {
        id: 21,
        image: '../static/images/images/beef.jpg',
        title: 'Beef',
        price: 350,
        quantity: 1
    },
    {
        id: 22,
        image: '../static/images/images/lamb.jpg',
        title: 'Lamb',
        price: 600,
        quantity: 1
    },
    {
        id: 23,
        image: '../static/images/images/vension.jpg',
        title: 'Vension',
        price: 650,
        quantity: 1
    },
    {
        id: 24,
        image: '../static/images/images/goat.jpg',
        title: 'Goat',
        price: 400,
        quantity: 1
    },
    {
        id: 25,
        image: '../static/images/images/chicken.jpg',
        title: 'Chicken',
        price: 250,
        quantity: 1
    },
    {
        id: 26,
        image: '../static/images/images/duck.jpg',
        title: 'Duck',
        price: 230,
        quantity: 1
    },
    {
        id: 27,
        image: '../static/images/images/rabbit.jpg',
        title: 'Rabbit',
        price: 330,
        quantity: 1
    },
    {
        id: 28,
        image: '../static/images/images/liver.jpg',
        title: 'Liver',
        price: 350,
        quantity: 1
    },
    {
        id: 29,
        image: '../static/images/images/sausage.jpg',
        title: 'Sausage',
        price: 230,
        quantity: 1
    },
    {
        id: 30,
        image: '../static/images/images/tuna.jpg',
        title: 'Tuna',
        price: 400,
        quantity: 1
    },
    {
        id: 31,
        image: '../static/images/images/trout.jpg',
        title: 'Trout',
        price: 700,
        quantity: 1
    },
    {
        id: 32,
        image: '../static/images/images/mackerel.jpg',
        title: 'Mackerel',
        price: 250,
        quantity: 1
    }
];
// Adding meat products to the existing fruitVegetableProducts array
const bakeryProducts = [
    {
        id: 33,
        image: '../static/images/images/whitebread.jpg',
        title: 'White Bread',
        price: 80,
        quantity: 1
    },
    {
        id: 34,
        image: '../static/images/images/ryebread.jpg',
        title: 'Rye Bread',
        price: 120,
        quantity: 1
    },
    {
        id: 35,
        image: '../static/images/images/baguette.jpg',
        title: 'Baguette Bread',
        price: 70,
        quantity: 1
    },
    {
        id: 36,
        image: '../static/images/images/sourdoughbread.jpg',
        title: 'Sourdough Bread',
        price: 100,
        quantity: 1
    },
    {
        id: 37,
        image: '../static/images/images/croissant.jpg',
        title: 'Croissant',
        price: 40,
        quantity: 1
    },
    {
        id: 38,
        image: '../static/images/images/turnover.jpg',
        title: 'Turnover',
        price: 70,
        quantity: 1
    },
    {
        id: 39,
        image: '../static/images/images/spongecake.jpg',
        title: 'Sponge Cake',
        price: 300,
        quantity: 1
    },
    {
        id: 40,
        image: '../static/images/images/cheesecake.jpg',
        title: 'Cheese Cake',
        price: 250,
        quantity: 1
    },
    {
        id: 41,
        image: '../static/images/images/cookies.jpg',
        title: 'Cookies',
        price: 165,
        quantity: 1
    },
    {
        id: 42,
        image: '../static/images/images/shortbread.jpg',
        title: 'Short Bread',
        price: 135,
        quantity: 1
    },
    {
        id: 43,
        image: '../static/images/images/applepie.jpg',
        title: 'Apple Pie',
        price: 220,
        quantity: 1
    },
    {
        id: 44,
        image: '../static/images/images/donut.jpg',
        title: 'Donut',
        price: 45,
        quantity: 1
    }
];
// Adding meat products to the existing fruitVegetableProducts array
const snacksProducts = [
    {
        id: 45,
        image: '../static/images/images/chips.jpg',
        title: 'Chips',
        price: 15,
        quantity: 1
    },
    {
        id: 46,
        image: '../static/images/images/pretzels.jpg',
        title: 'Pretzels',
        price: 80,
        quantity: 1
    },
    {
        id: 47,
        image: '../static/images/images/popcorn.jpg',
        title: 'Popcorn',
        price: 40,
        quantity: 1
    },
    {
        id: 48,
        image: '../static/images/images/crackers.jpg',
        title: 'Crackers',
        price: 25,
        quantity: 1
    },
    {
        id: 49,
        image: '../static/images/images/trail_mix.jpg',
        title: 'Trail Mix',
        price: 230,
        quantity: 1
    },
    {
        id: 50,
        image: '../static/images/images/sweets.jpg',
        title: 'Candy',
        price: 175,
        quantity: 1
    },
    {
        id: 51,
        image: '../static/images/images/icecream.jpg',
        title: 'Ice Cream',
        price: 35,
        quantity: 1
    },
    {
        id: 52,
        image: '../static/images/images/waterbottle.jpg',
        title: 'Water',
        price: 10,
        quantity: 1
    },
    {
        id: 53,
        image: '../static/images/images/orangejuice.jpg',
        title: 'Orange Juice',
        price: 15,
        quantity: 1
    },
    {
        id: 54,
        image: '../static/images/images/applejuice.jpg',
        title: 'Apple Juice',
        price: 15,
        quantity: 1
    },
    {
        id: 55,
        image: '../static/images/images/soda.jpg',
        title: 'Sodas',
        price: 20,
        quantity: 1
    },
    {
        id: 56,
        image: '../static/images/images/redbull.jpg',
        title: 'Redbull',
        price: 45,
        quantity: 1
    }
];
const dairyProducts = [
    {
        id: 57,
        image: '../static/images/images/Milk.jpeg',
        title: 'Milk',
        price: 40,
        quantity: 1
    },
    {
        id: 58,
        image: '../static/images/images/Feta.jpeg',
        title: 'Feta Cheese',
        price: 20,
        quantity: 1
    },
    {
        id: 59,
        image: '../static/images/images/Cheddar.jpeg',
        title: 'Cheddar Cheese',
        price: 30,
        quantity: 1
    },
    {
        id: 60,
        image: '../static/images/images/Mozzarella.jpeg',
        title: 'Mozzarella Cheese',
        price: 35,
        quantity: 1
    },
    {
        id: 61,
        image: '../static/images/images/Butter.jpeg',
        title: 'Butter',
        price: 50,
        quantity: 1
    },
    {
        id: 62,
        image: '../static/images/images/Yogurt.jpeg',
        title: 'Yogurt',
        price: 25,
        quantity: 1
    },
    {
        id: 63,
        image: '../static/images/images/Whipping_cream.jpeg',
        title: 'Whipping cream',
        price: 35,
        quantity: 1
    },
    {
        id: 64,
        image: '../static/images/images/Ghee.jpeg',
        title: 'Ghee',
        price: 45,
        quantity: 1
    },
    {
        id: 65,
        image: '../static/images/images/Cottage_Cheese.jpeg',
        title: 'Cottage Cheese',
        price: 20,
        quantity: 1
    }
];

const babyProducts = [
    {
        id: 66,
        image: '../static/images/johnsonoil.jpg',
        title: "Johnson's Baby Oil",
        price: 350,
        quantity: 1
    },
    {
        id: 67,
        image: '../static/images/Baby_Wipes.jpg',
        title: "Little's Baby Wipes",
        price: 70,
        quantity: 1
    },
    {
        id: 68,
        image: '../static/images/Moisturizer.jpg',
        title: 'Moisturizer',
        price: 470,
        quantity: 1
    },
    {
        id: 69,
        image: '../static/images/Baby_Shampoo.jpg',
        title: 'Himalaya Baby Shampoo',
        price: 330,
        quantity: 1
    },
    {
        id: 70,
        image: '../static/images/Baby_Powder.jpg',
        title: "Johnson's Baby Powder",
        price: 125,
        quantity: 1
    },
    {
        id: 71,
        image: '../static/images/Diapers.jpg',
        title: 'Pampers Baby Pants',
        price: 550,
        quantity: 1
    }
];

const medicineProducts = [
    {
        id: 72,
        image: '../static/images/images/panadol.jpg',
        title: 'Panadol',
        price: 60,
        quantity: 1
    },
    {
        id: 73,
        image: '../static/images/images/bruffen.jpg',
        title: 'Bruffen',
        price: 40,
        quantity: 1
    },
    {
        id: 74,
        image: '../static/images/images/zyrtec.jpg',
        title: 'Zyrtec',
        price: 35,
        quantity: 1
    },
    {
        id: 75,
        image: '../static/images/images/cataflam.jpg',
        title: 'Cataflam',
        price: 30,
        quantity: 1
    },
    {
        id: 76,
        image: '../static/images/images/osteocare.jpg',
        title: 'Osteocare',
        price: 70,
        quantity: 1
    },
    {
        id: 77,
        image: '../static/images/images/otrivin.png',
        title: 'Otrivin',
        price: 45,
        quantity: 1
    },
    {
        id: 78,
        image: '../static/images/images/feroglobin.png',
        title: 'Feroglobin',
        price: 45,
        quantity: 1
    },
    {
        id: 79,
        image: '../static/images/images/aspirin.jpg',
        title: 'Aspirin',
        price: 70,
        quantity: 1
    },
    {
        id: 80,
        image: '../static/images/images/motilium.jpg',
        title: 'Motilium',
        price: 45,
        quantity: 1
    }
];
const PopularPackges = [
    {
        id: 83,
        image: '../static/images/images/pack1.png',
        title: 'Green Garden Bundle',
        price: 350,
        quantity: 1
    },
    {
        id: 84,
        image: '../static/images/images/pack2.jpeg',
        title: 'Health Essentials Kit',
        price: 500,
        quantity: 1
    },
    {
        id: 85,
        image: '../static/images/images/pack3.jpeg',
        title: 'Butcher Choice Bundle',
        price: 35,
        quantity: 1
    },
    {
        id: 86,
        image: '../static/images/images/pack4.jpeg',
        title: 'Baby Essentials Bundle',
        price: 30,
        quantity: 1
    },
    {
        id: 87,
        image: '../static/images/images/pack5.jpeg',
        title: 'Baker Delight Box',
        price: 250,
        quantity: 1
    },
    {
        id: 88,
        image: '../static/images/images/pack6.jpeg',
        title: 'Snack Attack Bundle',
        price: 100,
        quantity: 1
    }
];
<<<<<<< HEAD
=======
const PopularPackges = [   
        {
            id: 83,
            image: '../static/images/images/pack1.png',
            title: 'Green Garden Bundle ',
            price: 350,
        },
        {
            id: 84,
            image: '../static/images/images/pack2.jpeg',
            title: 'Health Essentials Kit ',
            price: 500,
        },
        {
            id: 85,
            image: '../static/images/images/pack3.jpeg',
            title: 'Butcher Choice Bundle ',
            price: 35,
        },
        {
            id: 86,
            image: '../static/images/images/pack4.jpeg',
            title: 'Baby Essentials Bundle ',
            price: 30,
        },
        {
            id: 87,
            image: '../static/images/images/pack5.jpeg',
            title: 'Baker Delight Box ',
            price: 250,
        },
        {
            id: 88,
            image: '../static/images/images/pack6.jpeg',
            title: 'Snack Attack Bundle ',
            price: 100,
        }
    ];




>>>>>>> b295d94 (lol)

// Merge fruitVegetableProducts and meatProducts into a single categories array
const categories = [...fruitVegetableProducts, ...meatProducts, ...bakeryProducts, ...snacksProducts, ...dairyProducts, ...babyProducts, ...medicineProducts, ...PopularPackges];
let i = 0;
<<<<<<< HEAD
=======


>>>>>>> b295d94 (lol)
// Function to switch between displaying fruit/vegetable and meat products
function switchCategory(category) {
    let products = [];
    console.log("Category switched to:", category);
    switch (category) {
        case 'fruitVegetableProducts':
            products = fruitVegetableProducts;
            break;
        case 'meatProducts':
            products = meatProducts;
            break;
        case 'bakeryProducts':
            products = bakeryProducts;
            break;
        case 'snacksProducts':
            products = snacksProducts;
            break;
        case 'dairyProducts':
            products = dairyProducts;
            break;
        case 'babyProducts':
            products = babyProducts;
            break;
        case 'medicineProducts':
            products = medicineProducts;
            break;
        case 'PopularPackages':
            products = popularPackages;
            break;
        default:
            products = fruitVegetableProducts;
    }

    
    const root = document.getElementById('root');
    root.innerHTML = '';

    products.forEach(product => {
        root.innerHTML += `
            <div class="product">
                <img src="${product.image}" alt="${product.title}">
                <h3>${product.title}</h3>
                <p>$${product.price}</p>
                <button onclick="addToCart(${product.id})">Add to Cart</button>
            </div>
        `;
    });
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
    }else if (category === 'dairyProducts') {
        products = dairyProducts;
    }else if(category === 'babyProducts') {
        products = babyProducts;
    }else if(category === 'medicineProducts') {
        products = medicineProducts;
    }else if(category === 'PopularPackges') {
        products = PopularPackges;
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
                    <h2>LE ${price}.00</h2>
                    <button onclick='addtocart(${item.id})'>Add to cart</button>
                </div>
            </div>`
        );
    }).join('');
}
var cart = []; // This holds data sent to Flask
var dcart = []; // This holds data for display only

function addtocart(productId) {
    const selectedProduct = categories.find(item => item.id === productId);
    const itemIndex = cart.findIndex(item => item.id === productId);
    
    if (itemIndex > -1) {
        cart[itemIndex].quantity += 1;
    } else {
        // Add the product details to the cart
        const { id, title, image, price, quantity } = selectedProduct;
        cart.push({ id, title, image, price, quantity });
    }
    
    // Update the display-only cart (dcart)
    const displayItemIndex = dcart.findIndex(item => item.id === productId);
    if (displayItemIndex > -1) {
        dcart[displayItemIndex].quantity += 1;
    } else {
        dcart.push({ ...selectedProduct, quantity: 1 });
    }
    
    // Update the cart display
    displaycart();
    
    // Prepare cart data for Flask
    const cartDataForServer = cart.map(item => ({
        title: item.title,
        image: item.image,
        price: item.price,
        quantity: item.quantity
    }));
    
    // Send cart data to Flask
    fetch('/process_cart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ cart: cartDataForServer }), // Pass processed cart data
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to send cart data to server');
        }
        return response.json();
    })
    .then(data => {
        console.log(data); // Optional: Handle success response from server
        
        // Clear the cart after successfully sending data to server
        cart.length = 0;
        displaycart(); // Update cart display to show it's empty
    })
    .catch(error => {
        console.error('Error:', error); // Optional: Handle error case
    });
}

function delElement(a) {
    if (dcart[a].quantity > 1) {
        dcart[a].quantity -= 1;
    } else {
        dcart.splice(a, 1);
    }
    
    // Update the display-only cart (dcart)
    const indexInDcart = dcart.findIndex(item => item.id === cart[a].id);
    if (indexInDcart > -1) {
        dcart[indexInDcart].quantity -= 1;
        if (dcart[indexInDcart].quantity === 0) {
            dcart.splice(indexInDcart, 1);
        }
    }
    
    displaycart();
}

function displaycart() {
    let total = 0;
    document.getElementById("count").innerHTML = dcart.length;

    if (dcart.length === 0) {
        document.getElementById('cartItem').innerHTML = "Your cart is empty";
        document.getElementById("total").innerHTML = "LE " + 0 + ".00";
    } else {
        // Calculate the total price
        total = dcart.reduce((acc, item) => acc + (item.price * item.quantity), 0);
        document.getElementById("total").innerHTML = "LE " + total + ".00";

        // Display cart items on the client side
        document.getElementById("cartItem").innerHTML = dcart.map((item, index) => {
            return (
                `<div class='cart-item'>
                    <div class='row-img'>
                        <img class='rowimg' src=${item.image}>
                    </div>
                    <p style='font-size:12px;'>${item.title}</p>
                    <p style='font-size:12px;'>Quantity: ${item.quantity}</p>
                    <h2 style='font-size: 15px;'>LE ${item.price * item.quantity}.00</h2>
                    <i class='fa-solid fa-trash' onclick='delElement(${index})'></i>
                </div>`
            );
        }).join('');
    }
}

