function validateSignupForm() {
    var username = myform.username.value;
    var name =  myform.name.value;
    var email = myform.email.value;
    var password = myform.password.value;
    if (username == "") {
        alert("Userame must be filled out");
        return false;
    }
    if (name == "") {
        alert("Name must be filled out");
        return false;
    }
    if (email == "") {
        alert("Email must be filled out");
        return false;
    }
    if (password == "") {
        alert("password must be filled out");
        return false;
    }
    if (username.length < 4) {
        alert("username must be grater than 4 characters");
        return false;
    }
    if (password.length < 5) {
        alert("password must be grater than 5 characters");
        return false;
    }

}

function validateLoginForm() {
    var username = myform.username.value;
    var password = myform.password.value;
    if (username == "") {
        alert("Userame must be filled out");
        return false;
    }
    if (password == "") {
        alert("password must be filled out");
        return false;
    }
    if (username.length < 4) {
        alert("username must be grater than 4 characters");
        return false;
    }
    if (password.length < 5) {
        alert("password must be grater than 5 characters");
        return false;
    }
}