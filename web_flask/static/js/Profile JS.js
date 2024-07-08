// Define tab buttons and tab content elements
const tabBtn = document.querySelectorAll(".tab"); // Select all elements with class "tab"
const tab = document.querySelectorAll(".tabShow"); // Select all elements with class "tabShow"

// Function to handle tab switching
function tabs(panelIndex) {
    tab.forEach(function(node) {
        node.style.display = "none"; // Hide all tab content elements
    });
    tab[panelIndex].style.display = "block"; // Display the selected tab content element
}

tabs(0); // Show the first tab by default

// Add click event listener to tab buttons
$(".tab").click(function(){
    $(this).addClass("active").siblings().removeClass("active"); // Add "active" class to clicked tab button and remove it from other tab buttons
});

// Add event listeners to input elements
document.addEventListener("DOMContentLoaded", function() {
    const tabs = document.querySelectorAll(".tabShow"); // Select all elements with class "tabShow"

    tabs.forEach(function(tab) {
        const inputs = tab.querySelectorAll(".input"); // Select all input elements within the current tab

        inputs.forEach(function(input) {
            const placeholderText = input.getAttribute("placeholder"); // Get the placeholder text of the input element

            // Add focus event listener to input element
            input.addEventListener("focus", function() {
                if (this.value === '') {
                    this.placeholder = placeholderText; // Restore the placeholder text if the input value is empty
                }
            });

            // Add input event listener to input element
            input.addEventListener("input", function() {
                if (this.value !== '') {
                    this.placeholder = ''; // Remove the placeholder text if the input value is not empty
                }
            });

            // Add blur event listener to input element
            input.addEventListener("blur", function() {
                if (this.value === '') {
                    this.placeholder = placeholderText; // Restore the placeholder text if the input value is empty
                }
            });

            // Add keyup event listener to input element
            input.addEventListener("keyup", function(event) {
                if (event.key === 'Backspace' && this.value === '') {
                    this.placeholder = placeholderText; // Restore the placeholder text if the input value is empty and the Backspace key is pressed
                }
            });
        });
    });
});
// commented
