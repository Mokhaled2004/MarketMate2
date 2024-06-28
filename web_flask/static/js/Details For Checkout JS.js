function validate_form() {
    var name = document.getElementById("name").value;
    var phone = document.getElementById("phone").value;
    var email = document.getElementById("email").value;
    var pincode = document.getElementById("pincode").value;
    var error_message = document.getElementById("error_message");

    error_message.style.padding = "10px";

    var text;
    if (name.length < 3) {
        text = "Please enter a valid name.";
        error_message.innerHTML = text;
        return false;
    }
    if (isNaN(phone) || phone.length != 11) {
        text = "Please enter a valid phone number.";
        error_message.innerHTML = text;
        return false;
    }
    if (isNaN(pincode) || pincode.length != 5) { // Adjust pincode length if needed
        text = "Please enter a valid postal code.";
        error_message.innerHTML = text;
        return false;
    }
    if (email.indexOf("@") == -1 || email.length < 6) {
        text = "Please enter a valid email address.";
        error_message.innerHTML = text;
        return false;
    }
    return true;
}

// Ensure to attach this function to the form's onsubmit event
document.getElementById('paymentForm').onsubmit = validate_form;
