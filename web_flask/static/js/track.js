window.addEventListener('load', function() {
    // Set order status
    const statusDiv = document.getElementById('status');
    statusDiv.textContent = 'Order placed. Preparing for shipment...';

    // Generate a random delivery time between 0 and 24 hours
    const deliveryTimeHours = Math.floor(Math.random() * 25);
    const deliveryTimeSeconds = deliveryTimeHours * 3600;

    // Start timer for shipment to distributor (deliveryTimeSeconds for demo)
    startTimer(deliveryTimeSeconds, 'Time until delivery: ', function() {
        statusDiv.textContent = 'Order delivered!';
        document.getElementById('timer').textContent = '';
        document.getElementById('markDelivered').disabled = false;
        document.getElementById('markDelivered').classList.remove('hidden');
    });
});

document.getElementById('markDelivered').addEventListener('click', function() {
    document.getElementById('timer').classList.add('hidden');
    document.getElementById('markDelivered').classList.add('hidden');
    document.getElementById('status').classList.add('hidden');
    document.getElementById('thankYouMessage').classList.remove('hidden');
});

function startTimer(seconds, message, callback) {
    const timerDiv = document.getElementById('timer');
    let timeLeft = seconds;

    const interval = setInterval(() => {
        if (timeLeft > 0) {
            const hours = Math.floor(timeLeft / 3600);
            const minutes = Math.floor((timeLeft % 3600) / 60);
            const seconds = timeLeft % 60;
            timerDiv.textContent = `${message} ${hours}h ${minutes}m ${seconds}s`;
            timeLeft--;
        } else {
            clearInterval(interval);
            callback();
        }
    }, 1000);
}
