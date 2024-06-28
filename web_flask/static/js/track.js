window.addEventListener('load', function() {
    const statusDiv = document.getElementById('status');
    statusDiv.textContent = 'Order placed. Preparing for shipment...';

    // Set the duration for each stage to 3 seconds (3000 milliseconds)
    const stageDuration = 30; // in seconds

    const stages = [
        { stage: 'Order Placed', duration: stageDuration },
        { stage: 'Shipped', duration: stageDuration },
        { stage: 'Out for Delivery', duration: stageDuration },
        { stage: 'Delivered', duration: stageDuration },
    ];

    let currentStage = 0;
    updateStage(stages[currentStage].stage);

    startTimer(stages[currentStage].duration, `Time until ${stages[currentStage].stage.toLowerCase()}: `, function nextStage() {
        currentStage++;
        if (currentStage < stages.length) {
            updateStage(stages[currentStage].stage);
            startTimer(stages[currentStage].duration, `Time until ${stages[currentStage].stage.toLowerCase()}: `, nextStage);
        } else {
            document.getElementById('markDelivered').disabled = false;
            document.getElementById('markDelivered').classList.remove('hidden');
        }
    });
});

document.getElementById('markDelivered').addEventListener('click', function() {
    document.getElementById('timer').classList.add('hidden');
    document.getElementById('markDelivered').classList.add('hidden');
    document.getElementById('status').classList.add('hidden');
    document.getElementById('thankYouMessage').classList.remove('hidden');
});

// Add event listener for cancel button
document.getElementById('cancelOrder').addEventListener('click', function() {
    window.location.href = '/'; // Redirect to homepage
});

function startTimer(seconds, message, callback) {
    const timerDiv = document.getElementById('timer');
    let timeLeft = seconds;

    const interval = setInterval(() => {
        if (timeLeft > 0) {
            timerDiv.textContent = ${message} ${timeLeft}s;
            timeLeft--;
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

    const progress = document.querySelector('.progress::after');
    if (progress) {
        progress.style.width = ${(stageIndex[stage] / 3) * 100}%;
    }
}