function calculate() {
'use strict';
var volume;
var weight;
var length = document.getElementById('length').value;
var width = document.getElementById('width').value;
var height = document.getElementById('height').value;


length = Math.abs(length);
width = Math.abs(width);
height = Math.abs(height);

volume = length * width * height;
weight = volume * 62.4;


volume = volume.toFixed(1);
weight = weight.toFixed(1);


document.getElementById('volume').value = volume;
document.getElementById('weight').value = weight;

if(weight > 3000)
document.getElementById('weight').style.color = 'red';
else
document.getElementById('weight').style.color = 'black'; 

return false;
} 

function init() {
'use strict';
document.getElementById('myForm').onsubmit = calculate;
} 

function play(){
'use strict';
var song =document.getElementById("demo");
song.play();
} 

function pause(){
'use strict';
var song=document.getElementById("demo");
song.pause();
}

function volumeup(){
'use strict';
var song = document.getElementById("demo");
song.volume += 0.2;
}

function volumedown(){
'use strict';
var song = document.getElementById("demo");
song.volume -= 0.2;
}
window.onload = init;