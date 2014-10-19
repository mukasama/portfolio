function validateForm() {
    'use strict';
    var email = document.getElementById('email');
    var password = document.getElementById('password');
    if (email.value.length > 0) {
        return true;} 
    else {
        alert('Please complete the form!');
        return false;}
    if (password.value === "test-pass") {
        return true;} 
    else {
        alert('That is not the correct password!');
        return false;}
} 
function init() {
    'use strict';
    if (document && document.getElementById) {
        var loginForm = document.getElementById('loginForm');
        loginForm.onsubmit = validateForm;
    }
}
window.onload = init;