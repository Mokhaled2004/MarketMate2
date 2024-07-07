function validate_form(){
    var name=document.getElementById("name").value;
    var phone=document.getElementById("phone").value;
    var email=document.getElementById("email").value;
    var address=document.getElementById("address").value;
    var date=document.getElementById("date").value;
    var pincode=document.getElementById("pincode").value;
    var error_message=document.getElementById("error_message");

    error_message.style.padding="10px";

    var text;
    if(name.length<3){
        text="Please Enter a valid Name";
        error_message.innerHTML = text;
        return false;
    }
    if(isNaN(phone) || phone.length !=11){
        text="Please Enter a valid Phone Number";
        error_message.innerHTML=text;
        return false;
    }
   
    if(email.indexof("@") == -1 || email.length < 6){
        text="Please enter a valid E-mail ID.";
        error_message.innerHTML=text;
        return false;
    }
}


document.addEventListener('DOMContentLoaded', function() {
    // Fetch order details from the server
    fetch('/order_details')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Display order details
            const orderDetailsDiv = document.getElementById('order-details');
            if (data.length === 0) {
                orderDetailsDiv.innerHTML = '<p>No orders found</p>';
            } else {
                let orderDetailsHtml = '<h2>Order Details</h2>';
                data.forEach(order => {
                    orderDetailsHtml += `<p>Order ID: ${order.id}</p>`;
                    orderDetailsHtml += `<p>Order Date: ${order.created_at}</p>`;
                    orderDetailsHtml += `<p>Order Delivery Date: ${order.date}</p>`;
                    orderDetailsHtml += `<p>Total Price: ${order.total_price}</p>`;
                    orderDetailsHtml += `<p>Status: ${order.delivered}</p>`;
                    order.products.forEach(product => {
                        orderDetailsHtml += `<p>${product.title} - ${product.quantity} x ${product.price}</p>`;
                    });
                });
                orderDetailsDiv.innerHTML = orderDetailsHtml;
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
});


function selectMarket(market) {
    document.getElementById('market_name').value = market;
}
   // commented