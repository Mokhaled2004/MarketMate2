const tabBtn = document.querySelectorAll(".tab");
const tab = document.querySelectorAll(".tabShow");

function tabs(panelIndex) {
    tab.forEach(function(node) {
        node.style.display = "none";
    });
    tab[panelIndex].style.display = "block";
}

tabs(0);

$(".tab").click(function(){
    $(this).addClass("active").siblings().removeClass("active");
});

// Example input behavior
document.addEventListener("DOMContentLoaded", function() {
    const tabs = document.querySelectorAll(".tabShow");

    tabs.forEach(function(tab) {
        const inputs = tab.querySelectorAll(".input");

        inputs.forEach(function(input) {
            const placeholderText = input.getAttribute("placeholder");

            input.addEventListener("focus", function() {
                if (this.value === '') {
                    this.placeholder = placeholderText;
                }
            });

            input.addEventListener("input", function() {
                if (this.value !== '') {
                    this.placeholder = '';
                }
            });

            input.addEventListener("blur", function() {
                if (this.value === '') {
                    this.placeholder = placeholderText;
                }
            });

            input.addEventListener("keyup", function(event) {
                if (event.key === 'Backspace' && this.value === '') {
                    this.placeholder = placeholderText;
                }
            });
        });
    });
});
