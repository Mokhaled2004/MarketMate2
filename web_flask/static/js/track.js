window.addEventListener('load', function() {
    const statusDiv = document.getElementById('status');
    statusDiv.textContent = 'Order placed. Preparing for shipment...';

    const stageDuration = 3; // in seconds
    const stages = [
        { stage: 'Order Placed', duration: stageDuration },
        { stage: 'Shipped', duration: stageDuration },
        { stage: 'Out for Delivery', duration: stageDuration },
        { stage: 'Delivered', duration: stageDuration },
    ];

    let currentStage = getCurrentStageFromStorage() || 0;
    let timeLeft = localStorage.getItem('timeLeft') || stages[currentStage].duration;

    updateStage(stages[currentStage].stage);

    startTimer(timeLeft, `Time until ${stages[currentStage].stage.toLowerCase()}: `, function nextStage() {
        currentStage++;
        if (currentStage < stages.length) {
            updateStage(stages[currentStage].stage);
            if (stages[currentStage].stage === 'Delivered') { // Added condition for "Delivered" stage
                clearCurrentStageFromStorage();
                localStorage.removeItem('timeLeft');
                //document.getElementById('markDelivered').disabled = false;
              //document.getElementById('markDelivered').classList.remove('hidden');
                document.getElementById('timer').classList.add('hidden');
                document.getElementById('status').classList.add('hidden');
                document.getElementById('markDelivered').disabled = false;
                document.getElementById('markDelivered').classList.remove('hidden');
                document.getElementById('thankYouMessage').classList.remove('hidden');
                document.getElementById('order-details').innerHTML = '<h2>Order Details</h2>'; // Remove order details
                localStorage.removeItem('timeLeft');
                document.querySelector('#order-details').innerHTML += '<div style="font-size: 1em; font-weight: bold;">Delivered</div>'; // Add "Delivered" message
            } else {
                startTimer(stages[currentStage].duration, `Time until ${stages[currentStage].stage.toLowerCase()}: `, nextStage);
                saveCurrentStageToStorage(currentStage);
            }
    }
});

document.getElementById('markDelivered').addEventListener('click', function() {
    this.innerText = 'Delivered!';
    // Optionally, update UI or perform further actions
});

document.getElementById('cancelOrder').addEventListener('click', function() {
    this.innerText = 'Cancelled!';
    // Optionally, update UI or perform further actions
});


    function startTimer(seconds, message, callback) {
        const timerDiv = document.getElementById('timer');
        let timeLeft = seconds;

        const interval = setInterval(() => {
            if (timeLeft > 0) {
                timerDiv.textContent = `${message} ${timeLeft}s`;
                timeLeft--;
                localStorage.setItem('timeLeft', timeLeft);
            } else {
                clearInterval(interval);
                callback();
            }
        }, 1000);
    }

    function updateStage(stage) {
        const stageIndex = {
            'Order Placed': 0,
            'Shipped': 1,
            'Out for Delivery': 2,
            'Delivered': 3
        };

        document.getElementById('status').textContent = stage;
        document.querySelectorAll('.circle').forEach((circle, index) => {
            if (index <= stageIndex[stage]) {
                circle.classList.add('active');
            } else {
                circle.classList.remove('active');
            }
        });

        document.querySelectorAll('.status-messages div').forEach((message, index) => {
            if (index <= stageIndex[stage]) {
                message.classList.add('active');
            } else {
                message.classList.remove('active');
            }
        });

        const progress = document.querySelector('.progress');
        if (progress) {
            progress.style.width = `${(stageIndex[stage] / 3) * 100}%`;
        }
    }

    function getCurrentStageFromStorage() {
        return localStorage.getItem('currentStage') ? parseInt(localStorage.getItem('currentStage')) : null;
    }

    function saveCurrentStageToStorage(stage) {
        localStorage.setItem('currentStage', stage);
    }

    function clearCurrentStageFromStorage() {
        localStorage.removeItem('currentStage');
    }
});



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

document.getElementById('markDelivered').addEventListener('click', function() {
    fetch(`/mark_delivered`, {
        method: 'PUT'
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to update order status');
        }
        
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to update order status');
    });
});

document.getElementById('cancelOrder').addEventListener('click', function() {
    fetch(`/mark_cancelled`, {
        method: 'PUT'
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to update order status');
        }
        
        
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to update order status');
    });
});

// Add event listeners to all buttons with the 'pressed' class
document.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', function() {
        // Toggle the 'pressed' class on the clicked button
        this.classList.toggle('pressed');
    });
});
//commented


