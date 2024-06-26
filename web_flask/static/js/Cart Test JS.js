const product = [
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
 const categories = [...new Set(product.map((item)=>
    {return item}))]
    let i=0;
 document.getElementById('root').innerHTML = categories.map((item)=>
 {
    var {image, title, price} = item;
    return(
        `<div class='box'>
            <div class='img-box'>
                <img class='images' src=${image}></img>
            </div>
        <div class='bottom'>
        <p>${title}</p>
        <h2>$ ${price}.00</h2>`+
        "<button onclick='addtocart("+(i++)+")'>Add to cart</button>"+
        `</div>
        </div>`
    )
 }).join('')
 
 var cart =[];
 
 function addtocart(a){
    const itemIndex = cart.findIndex(item => item.id === categories[a].id);
    if (itemIndex > -1) {
        cart[itemIndex].quantity += 1;
    } else {
        cart.push({...categories[a], quantity: 1});
    }
    displaycart();
 }
 
 function delElement(a){
    if (cart[a].quantity > 1) {
        cart[a].quantity -= 1;
    } else {
        cart.splice(a, 1);
    }
    displaycart();
 }
 
 function displaycart(){
    let j = 0, total=0;
    document.getElementById("count").innerHTML = cart.length;
    if(cart.length==0){
        document.getElementById('cartItem').innerHTML = "Your cart is empty";
        document.getElementById("total").innerHTML = "$ "+0+".00";
    }
    else{
        document.getElementById("cartItem").innerHTML = cart.map((items)=>
        {
            var {image, title, price, quantity} = items;
            total=total+(price * quantity);
            document.getElementById("total").innerHTML = "$ "+total+".00";
            return(
                `<div class='cart-item'>
                <div class='row-img'>
                    <img class='rowimg' src=${image}>
                </div>
                <p style='font-size:12px;'>${title}</p>
                <p style='font-size:12px;'>Quantity: ${quantity}</p>
                <h2 style='font-size: 15px;'>$ ${price * quantity}.00</h2>`+
                "<i class='fa-solid fa-trash' onclick='delElement("+ (j++) +")'></i></div>"
            );
        }).join('');
    }
 }
 