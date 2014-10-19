var totalPoints = 0;

var valueM = 0;
var valueS = 0;
var valueU = 0;

function randomize() {
	valueM = Math.floor((Math.random()*18)+2);
	valueS = Math.floor((Math.random()*10)+2);
	valueU = Math.floor((Math.random()*10)+2);

	document.getElementById('pickM').value = +valueM;
	document.getElementById('pickS').value = +valueS;
	document.getElementById('pickU').value = +valueU;
	document.getElementById('myattrpoints').value = 0;
	
	totalPoints = +valueM + +valueS + +valueU;
}

function takeaway(attrNum) {
	var myattrpoints = parseInt(document.getElementById('myattrpoints').value);
	
	if ((myattrpoints < totalPoints) && (window['value'+attrNum] > 0)) {
	var attrPoints = document.getElementById('pick' + attrNum).value;
	document.getElementById('pick' + attrNum).value = attrPoints - 1;
	document.getElementById('myattrpoints').value = myattrpoints + 1;
	window['value'+attrNum] = window['value'+attrNum] - 1;
	}
	else{
	alert('Error! Not enough points to subtract. Minimum points have been reached. All attributes must be > 0.')
	}
}

function addition(attrNum) {
	var myattrpoints = parseInt(document.getElementById('myattrpoints').value);
	
	if (myattrpoints > 0) {
	var attrPoints = parseInt(document.getElementById('pick' + attrNum).value);
	document.getElementById('pick' + attrNum).value = attrPoints + 1;
	document.getElementById('myattrpoints').value = myattrpoints - 1;
	window['value'+attrNum] = window['value'+attrNum] + 1;
	}
	else{
	alert('Error! Not enough points to add! Take points from another to add to this attribute.');
	}
}

function beginroll() {
	'use strict';
	randomize();
}

window.onload = beginroll();


