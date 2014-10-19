function init(){
	'use strict';
	
	var firstName = COOKIE.getCookie('firstName');
	var lastName = COOKIE.getCookie('lastName');
	document.getElementById('display').innerHTML = "Thanks for your business " + firstName + " " + lastName + "!";
	

	var product1 = parseInt(COOKIE.getCookie('product1'),10);
	var product2 = parseInt(COOKIE.getCookie('product2'),10);
	var product3 = parseInt(COOKIE.getCookie('product3'),10);
	var maxquan = product1 + product2 + product3;
	var maxcost = (product1 * 35.95) + (product2 * 105.60) + (product3 * 59.99);
	maxcost = maxcost.toFixed(2);
	
	document.getElementById('maxcost').innerHTML = maxcost;
	document.getElementById('maxquan').innerHTML = maxquan;	
}

window.onload = init;
