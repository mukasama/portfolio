// JavaScript Document

var imagesList = [];
imagesList[0] = "images/work.jpg";
imagesList[1] = "images/question1.jpg";
imagesList[2] = "images/family.jpg";
imagesList[3] = "images/mother.jpg";
imagesList[4] = "images/bed.jpg";
imagesList[5] = "images/courage.jpg";
imagesList[6] = "images/question3.jpg";
imagesList[7] = "images/dream.png";

var textColorsList = [];
textColorsList [000] = "#FF0000"; //red
textColorsList [001] = "#FF7F00"; //orange
textColorsList [002] = "#0000FF"; //blue
textColorsList [003] = "#8F00FF "; //violet
textColorsList [0004] = "#254117"; //dark green
textColorsList [0005] = "#808000"; //Olive
textColorsList [0006] = "#A55D35"; //brown
textColorsList [0007] = "#000000"; //black

var page = 07;

var story = [];

story[00] = new Object();
story[00].text = "Johnny's mother had just come back home from work. Do you want Johnny to ask his mother a question?";
story[00].DestinationA = 02;
story[00].DestinationB = 03;
story[00].isHiddenA = false;
story[00].isHiddenB = false;
story[00].image = imagesList[0];
story[00].textColor = textColorsList[000];

story[03] = new Object();
story[03].text = "Are you sure you don't want to ask the question? It might be an important one?";
story[03].DestinationA = 07;
story[03].DestinationB= 07;
story[03].isHiddenA = false;
story[03].isHiddenB = true;
story[03].image = imagesList[1];
story[03].textColor = textColorsList[001];

story[02] = new Object();
story[02].text = "Johnny asked his mother: Mum, why are some of youre hairs turning grey? Do you want to see what his mother's response was?";
story[02].DestinationA = 04;
story[02].DestinationB = 06;
story[02].isHiddenA = false;
story[02].isHiddenB = false;
story[02].image = imagesList[2];
story[02].textColor = textColorsList[002];

story[06] = new Object();
story[06].text = "Really, you had the courage to ask such an interesting question; now you dont want to see the responce!";
story[06].DestinationA = 07;
story[06].DestinationB = 07;
story[06].isHiddenA = false;
story[06].isHiddenB = true;
story[06].image = imagesList[5];
story[06].textColor = textColorsList[003];

story[04] = new Object();
story[04].text = "From the kitchen the mother replied: Its because of you dear! Every bad action of your's will turn one of my hairs grey! Do you want to read what Johnny's reaction was?";
story[04].DestinationA = 05;
story[04].DestinationB = 01;
story[04].isHiddenA = false;
story[04].isHiddenB = false;
story[04].image = imagesList[3];
story[04].textColor = textColorsList[004];

story[01] = new Object();
story[01].text = "Are you sure? Kid's do have funny responces?";
story[01].DestinationA = 07;
story[01].DestinationB = 07;
story[01].isHiddenA = false;
story[01].isHiddenB = true;
story[01].image = imagesList[6];
story[01].textColor = textColorsList[005];

story[05] = new Object();
story[05].text = "Oh his way to bed: Johnny replied, Now I know why grandmother has only grey hairs on her head! Haha...";
story[05].DestinationA = 07;
story[05].DestinationB= 07;
story[05].isHiddenA = false;
story[05].isHiddenB = true;
story[05].image = imagesList[4];
story[05].textColor = textColorsList[006];

story[07]= new Object();
story[07].text= "It was all just a dream! THE END...";
story[07].DestinationA = 00;
story[07].DestinationB = 00;
story[07].isHiddenA = false;
story[07].isHiddenB = true;
story[07].image = imagesList[7];
story[07].textColor = textColorsList[007];

// Choices for buttons
 
story[00].buttonA = "Yes";
story[00].buttonB = "No";

story[01].buttonA = "Continue";
story[01].buttonB = "End.";

story[02].buttonA = "Yes";
story[02].buttonB = "No";
 
story[03].buttonA = "Continue";
story[03].buttonB = "End.";

story[04].buttonA = "Yes";
story[04].buttonB = "No";
 
story[05].buttonA = "Continue";
story[05].buttonB = "End.";
 
story[06].buttonA = "Continue";
story[06].buttonB = "End.";

story[07].buttonA = "Continue";
story[07].buttonB = "End";

var page = 07

// My Functions

function OnPress(buttonPressed)
{
	if (page == 07)
	{
		page = 00;
	}
	else if (buttonPressed == 'A')
	{
		page = story[page].DestinationA;
	}
	else if  (buttonPressed == 'B')
	{
 		page = story[page].DestinationB;
	}
	
	document.getElementById("story").innerHTML = story[page].text;
	document.getElementsByName('NavGameA')[00].value = story[page].buttonA;
	document.getElementsByName('NavGameB')[00].value = story[page].buttonB;
	document.getElementsByName('NavGameA')[00].hidden = story[page].isHiddenA;
	document.getElementsByName('NavGameB')[00].hidden = story[page].isHiddenB;

	document.getElementById("image").src = story[page].image;
	
	document.getElementById("story").style.color = story[page].textColor;
}