function myCookies(){
	'use strict';
	
	var firstName = document.getElementById('firstName').value;
	var lastName = document.getElementById('lastName').value;
	var address = document.getElementById('address').value;
	var city = document.getElementById('city').value;
	var state = document.getElementById('state').value;
	var zipCode = document.getElementById('zipCode').value;
	var phoneNumber = document.getElementById('phoneNumber').value;
	
	var constract = new Date();

	expiration.setDate(expiration.getDate() + 1);//Tomorrow
	COOKIE.setCookie('firstName', firstName, constract);
	COOKIE.setCookie('lastName', lastName, constract);
	COOKIE.setCookie('address', address, constract);
	COOKIE.setCookie('city', city, constract);
	COOKIE.setCookie('state', state, constract);
	COOKIE.setCookie('zipCode', zipCode, constract);
	COOKIE.setCookie('phoneNumber', phoneNumber, constract);
	
}

function init(){
	'use strict';
	var cart = document.getElementById('cart');
	cart.onsubmit = myCookies;
}
window.onload = init;
