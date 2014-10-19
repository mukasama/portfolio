// JavaScript Document

function gradeTotal(){
	'use strict';
	
	var type = 'type';
	
	var exerWeight = document.getElementById('exercises');
	var mpWeight = document.getElementById('mp');
	var finalWeight = document.getElementById('final');
	
	var exerTot = 0;
	var mpTot = 0;
	var finalTot = 0;
	
	var exerCt = 0;
	var mpCt = 0;
	var finalCt = 0;
	
	var grade1 = document.getElementById('grade1');
	var grade1Type = document.getElementById('type1').value;
	var field1 = document.getElementById('field1').value;
	var grade2 = document.getElementById('grade2');
	var grade2Type = document.getElementById('type2').value;
	var field2 = document.getElementById('field2').value;
	var grade3 = document.getElementById('grade3');
	var grade3Type = document.getElementById('type3').value;
	var field3 = document.getElementById('field3').value;
	var grade4 = document.getElementById('grade4');
	var grade4Type = document.getElementById('type4').value;
	var field4 = document.getElementById('field4').value;

	//converts variables to integers
	if (exerWeight && exerWeight.value){
		exerWeight = parseInt(exerWeight.value, 10);
	}	
	if (mpWeight && mpWeight.value){
		mpWeight = parseInt(mpWeight.value, 10);
	}
	if (finalWeight && finalWeight.value){
		finalWeight = parseInt(finalWeight.value, 10);
	}
	
	if (grade1 && grade1.value){
		grade1 = parseInt(grade1.value, 10);
	}
	if (grade2 && grade2.value){
		grade2 = parseInt(grade2.value, 10);
	}
	if (grade3 && grade3.value){
		grade3 = parseInt(grade3.value, 10);
	}
	if (grade4 && grade4.value){
		grade4 = parseInt(grade4.value, 10);
	}
	
	//Validation step
	if(isNaN(exerWeight)){
		alert("Please enter numbers in the EXERCISE'S Rubric.");
		return false;
	}
	if(isNaN(mpWeight)){
		alert("Please enter numbers in the MINI-PROJECT'S Rubric.");
		return false;
	}
	if(isNaN(finalWeight)){
		alert("Please enter numbers in the FINAL'S Rubric.");
		return false;
	}
	if((exerWeight + mpWeight + finalWeight) != 100){
		alert("'The total number of grades in the RUBRIC must add up to 100.");
		return false;
	}
	if (field1.length > 20){
		alert ("Enter no more than 20 characters for Grade 1.");
		return false;
	}
	if (field2.length > 20){
		alert ("Enter no more than 20 characters for Grade 2.");
		return false;
	}
	if (field3.length > 20){
		alert ("Enter no more than 20 characters for Grade 3.");
		return false;
	}
	if (field4.length > 20){
		alert ("Enter no more than 20 characters for Grade 4.");
		return false;
	}
	if (isNaN(grade1)){
		alert("This is not a number. Please enter a number for Grade 1.");
		return false;
	}
	if (isNaN(grade2)){
		alert("This is not a number. Please enter a number for Grade 2.");
		return false;
	}
	if (isNaN(grade3)){
		alert("This is not a number. Please enter a number for Grade 3.");
		return false;
	}
	if (isNaN(grade4)){
		alert("This is not a number. Please enter a number for Grade 4.");
		return false;
	}

	console.log(grade1Type.value);
	console.log(grade2Type);
	console.log(grade1);
	switch(grade1Type){
		case 'exercises':
			exerCt += 1;
			exerTot += grade1;
			break;
		case 'mp':
			mpCt += 1;
			mpTot += grade1;
			break;
		case 'final':
			finalCt += 1;
			finalTot += grade1;	
			break;		
	}
	switch(grade2Type){
		case 'exercises':
			exerCt += 1;
			exerTot += grade2;
			break;
		case 'mp':
			mpCt += 1;
			mpTot += grade2;
			break;
		case 'final':
			finalCt += 1;
			finalTot += grade2;	
			break;		
	}
	switch(grade3Type){
		case 'exercises':
			exerCt += 1;
			exerTot += grade3;
			break;
		case 'mp':
			mpCt += 1;
			mpTot += grade3;
			break;
		case 'final':
			finalCt += 1;
			finalTot += grade3;	
			break;
	}
	switch(grade4Type){
		case 'exercises':
			exerCt += 1;
			exerTot += grade4;
			break;
		case 'mp':
			mpCt += 1;
			mpTot += grade4;
			break;
		case 'final':
			finalCt += 1;
			finalTot += grade4;	
			break;
	}
	//Calculates weights, leaves zero if there are no grades
	console.log(exerCt);
	console.log(mpCt);
	console.log(finalCt);
	console.log(exerTot);
	console.log(mpTot);
	console.log(finalTot);
	if (exerCt != 0){
		exerWeight = (exerTot / exerCt) * exerWeight;
	}
	else{exerWeight = 0;}
	if (mpCt != 0){
		mpWeight = (mpTot / mpCt) * mpWeight;
	}
	else{mpWeight = 0;}
	if (finalCt != 0){
		finalWeight = (finalTot / finalCt) * finalWeight;
	}
	else{finalWeight =0;}
	console.log(exerWeight);
	console.log(mpWeight);
	console.log(finalWeight);
	var total = exerWeight/100 + mpWeight/100 + finalWeight/100;
	
	document.getElementById('total').value = total.toFixed(2);
	return false;
}

function init(){
	'use strict';
	var grades = document.getElementById('mygrades');
	grades.onsubmit = gradeTotal;
}

window.onload = init;
