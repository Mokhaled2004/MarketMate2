function searchText() {
    // Get the search input value
    var searchText = document.getElementById('searchText').value.toLowerCase();

    // Define the specific text and its corresponding URL
    var redirects = {
        "fruits": 'C:\Users\Owner\.vscode\programs\MarketMate2\web_flask\templates\Cart Test HTML.html',
        // Add more specific texts and their corresponding URLs as needed
    };

    // Check if the entered text matches the specific text
    if (searchText in redirects) {
        // Redirect to the corresponding URL
        window.location.href = redirects[searchText];
    } else {
        // Handle case when no match is found (optional)
        alert("No specific page found for: " + searchText);
        // You can add additional handling here, like showing an error message
    }
}
