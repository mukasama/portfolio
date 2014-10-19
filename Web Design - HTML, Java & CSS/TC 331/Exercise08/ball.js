var canvas;
var ctx;

var width  = 320;
var height = 240;

var speedX 	= 0; 	//how fast the ball is moving in the horizontal direction
var speedY 	= 0; 	//how fast the ball is moving in the vertical direction

var radius 	= 10;

var x 	= width  / 2  - radius;  //starting horizontal position
var y 	= height / 2  - radius;  //starting vertical position

var circleColor	= "#FFFFFF";
var rectangleColorBg = "#FF0000";
var rectangleColorStroke = "#000000";

function speed(m){
	'use strict';
	m = m || event;
	
	var key = m.keyCode;
	
	
	
	switch(key){
		case 115: 
			if(speedY<5){
				speedY += .80;
				console.log(speedY+" : S");
				break;
			}
			
		case 100: 
			if(speedX<5){
				speedX += .80;
				console.log(speedX+" : D");
				break;
			}

		case 119: 
			if(speedY>(-5)){
				speedY -= .80;
				console.log(speedY+" : W");
				break;
			}

		case 97: 
			if(speedX>(-5)){
				speedX -= .80;
				console.log(speedX+" : A");
				break;
			}			
	}

	return false;	
}

function init() {
	canvas = document.getElementById("canvas");
	ctx = canvas.getContext("2d");
	return setInterval(draw, 1);
}

function circle(x,y,r, color) {
	ctx.fillStyle = color;
	ctx.beginPath();
	ctx.arc(x, y, r, 0, Math.PI*2, true);
	ctx.fill();
}

function rect(x,y,w,h) {
	ctx.fillStyle 	= rectangleColorBg;
  	ctx.strokeStyle = rectangleColorStroke;
	ctx.beginPath();
	ctx.rect(x,y,w,h);
	ctx.closePath();
	ctx.fill();
	ctx.stroke();
}

function draw() {
    'use strict';

    x += speedX;
    if (x >= (width - radius)) {
        x += --speedX;
    }
    if (x <= (0 + radius)) {
        x += ++speedX;
    }
    
    y += speedY;
    if (y >= (height - radius)) {
        y += --speedY;
    }
    if (y <= (0 + radius)) {
       y += ++speedY;
    }
    
    rect(0,0,width,height);
    circle(x, y, radius, circleColor);
}

window.addEventListener('keypress', speed, false);
window.onload = init;
