function validate(){
    var name=document.getElementById("name").value;
    var phone=document.getElementById("phone").value;
    var email=document.getElementById("email").value;
    var error_message=document.getElementById("error_message");

    error_message.style.padding="10px";

    var text;
    if (name.length < 3) {
        text = "Please enter a valid name (at least 3 characters).";
        error_message.innerHTML = text;
        return false;
    }

    // Validate Phone Number (assuming Egypt format: 10 digits starting with 01)
    if (isNaN(phone) || phone.length != 11 || !phone.startsWith("01")) {
        text = "Please enter a valid Egyptian phone number (11 digits starting with 01).";
        error_message.innerHTML = text;
        return false;
    }

    // Validate Email
    if (email.indexOf("@") == -1 || email.length < 6) {
        text = "Please enter a valid email address.";
        error_message.innerHTML = text;
        return false;
    }
    
}
   // commented

