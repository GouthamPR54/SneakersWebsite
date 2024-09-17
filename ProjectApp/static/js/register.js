function register() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var contactno = document.getElementById("contact").value;
    var password = document.getElementById("password").value;

    if (name === "") {
        alert("Please Enter Name");
        return false;
    }
    if (email === "") {
        alert("Please Enter Email");
        return false;
    }
    if (!isValidEmail(email)) {
        alert("Please Enter a Valid Email Address");
        return false;
    }
    if (contactno === "") {
        alert("Please Enter Contact No");
        return false;
    }
    if (password === "") {
        alert("Please Enter Password");
        return false;
    }
    if (!isValidPassword(password)) {
        alert("Please Enter a Valid Password (at least 8 characters, including letters and numbers)");
        return false;
    }

    return true;
}

// Function to check if the email is in a valid format
function isValidEmail(email) {
    // Regular expression for a basic email validation
    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
}

// Function to check if the password is in a valid format
function isValidPassword(password) {
    // Regular expression for a password with at least 8 characters, including letters and numbers
    var passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    return passwordPattern.test(password);
}
