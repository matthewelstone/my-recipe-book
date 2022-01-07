$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
});




var password = document.getElementById("password");
var confirmPassword = document.getElementById("confirmPassword");

function validatePassword(){
    if(password.value != confirmPassword.value){
        confirmPassword.setCustomValidity("Passwords Don't Match");
    } else {
        confirmPassword.setCustomValidity("");
    }
}
password.onchange = validatePassword;
confirmPassword.onkeyup = validatePassword;



function confirmLogout(){
    var agree = confirm("Are you sure?");

    if(agree){
        return true;
    } else {
        return false;
    }
}

