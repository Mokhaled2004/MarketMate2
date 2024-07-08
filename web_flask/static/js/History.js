document.addEventListener('DOMContentLoaded', function () {
    const orderList = document.getElementById('order-list');

    // Function to fetch order history based on filter
    function fetchOrders(filter) {
        fetch(`/fetch_filtered_orders?filter=${filter}`)
            .then(response => response.json())
            .then(orders => {
                orderList.innerHTML = ''; // Clear previous list items
                orders.forEach(order => {
                    const li = document.createElement('li');
                    
                    // Build the HTML for the products
                    let productsHtml = '<ul>';
                    order.products.forEach(product => {
                        productsHtml += `
                            <li>
                                <p><strong>Title:</strong> ${product.title}</p>
                                <p><strong>Price:</strong> $${product.price}</p>
                                <p><strong>Quantity:</strong> ${product.quantity}</p>
                            </li>
                        `;
                    });
                    productsHtml += '</ul>';
    
                    // Build the HTML for the order
                    li.innerHTML = `<strong>Order ID:</strong> ${order.id}<br>
                                    <strong>Order Creation Date:</strong> ${order.created_at}<br>
                                    <strong>Order Delivery Date:</strong> ${order.date}<br>
                                    <strong>Order Items:</strong> ${productsHtml}<br>
                                    <strong>Total Price:</strong> $${order.total_price}<br>
                                    <strong>Address:</strong> ${order.address}<br>
                                    <strong>Market Name:</strong> ${order.market_name}<br>
                                    <strong>Order Status:</strong> ${order.delivered}<br>
                                    <hr>`;
                    orderList.appendChild(li);
                });
            })
            .catch(error => console.error('Error fetching order history:', error));
    }
    

    // Event listener for dropdown menu items
    document.querySelectorAll('.dropdown-content a').forEach(item => {
        item.addEventListener('click', function(event) {
            event.preventDefault();
            const filter = this.getAttribute('data-filter');
            fetchOrders(filter);
        });
    });

    // Initially fetch all orders
    fetchOrders('all');
});
   // commented
