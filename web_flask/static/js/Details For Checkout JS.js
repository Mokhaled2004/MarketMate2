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
<<<<<<< HEAD
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
=======
    function validatePhoneNumber(phone) {
        var text = "";
        var error_message = document.getElementById('error_message'); // Assuming you have an element with id 'error_message' to display the error
        
        // Check if phone is not a number or if its length is not 11
        if(isNaN(phone) || phone.length !== 11){
            text = "Please Enter a valid Egyptian Phone Number"; // Adjusted message for Egyptian phone number
            error_message.innerHTML = text;
            return false;
        }
        
        // Additional checks if needed (e.g., specific starting digits, etc.)
        
        // Clear error message if validation passes
        error_message.innerHTML = "";
        
        return true;
    }
    
function validatePincode(pincode) {
    var text = "";
    var error_message = document.getElementById('error_message'); // Assuming you have an element with id 'error_message' to display the error
    
    // Check if pincode is not a number or if its length is not 5
    if(isNaN(pincode) || pincode.length !== 5){
        text = "Please enter a valid 5-digit Pincode"; // Adjusted message for 5-digit pin code
        error_message.innerHTML = text;
        return false;
    }
    
    // Additional checks if needed (e.g., specific starting digits, etc.)
    
    // Clear error message if validation passes
    error_message.innerHTML = "";
    
    return true;
}

    if(email.indexof("@") == -1 || email.length < 6){
        text="Please enter a valid E-mail ID.";
        error_message.innerHTML=text;
>>>>>>> main
        return false;
    }
    return true;
}

// Ensure to attach this function to the form's onsubmit event
document.getElementById('paymentForm').onsubmit = validate_form;
