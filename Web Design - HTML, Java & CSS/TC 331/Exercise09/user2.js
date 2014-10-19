function checkOut(){
	'use strict';
	
	var product1 = document.getElementById('product1').value;
	var product2 = document.getElementById('product2').value;
	var product3 = document.getElementById('product3').value;
	
	var expiration = new Date();
	expiration.setDate(expiration.getDate() + 1);
	
	COOKIE.setCookie('product1', product1, expiration);
	COOKIE.setCookie('product2', product2, expiration);
	COOKIE.setCookie('product3', product3, expiration);
	
	if (product1 > 0 || product2 > 0 || product3 > 0){
		var total = parseInt(COOKIE.getCookie('product1'), 10) + parseInt(COOKIE.getCookie('product2'), 10) + parseInt(COOKIE.getCookie('product3'), 10);
		window.location="checkout.html";
	}

}

function init(){
	'use strict';
	
	var firstName = COOKIE.getCookie('firstName');
	var lastName = COOKIE.getCookie('lastName');
	var showname = document.getElementById('showname');
	showname.innerHTML = 'Hello ' + firstName + ' ' + lastName;
}

window.onload = init;