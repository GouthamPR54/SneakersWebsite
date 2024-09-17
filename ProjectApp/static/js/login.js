function loginvalidation() {
    var email = document.getElementById("email").value.trim();  // Trim leading/trailing spaces
    var password = document.getElementById("password").value.trim();  // Trim leading/trailing spaces

    if (email === "") {
        alert("Please Enter Email");
        return false;
    }
    if (password === "") {
        alert("Please Enter Password");
        return false;
    }

    // // Add logic for checking incorrect email or password here
    // // For demonstration purposes, let's assume a simple condition for incorrect credentials
    // if (email.toLowerCase() !== "example@email.com" || password !== "password") {
    //     alert("Incorrect email or password");
    //     return false;
    // }

    // If all checks pass, return true to allow form submission
    return true;
}
