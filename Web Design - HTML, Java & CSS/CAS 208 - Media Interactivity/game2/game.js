// JavaScript Document

var page = 07;
var story = [];

story[00] = new Object();
story[00].text = "Johnny's mother had just come back home from work. Do you want Johnny to ask his mother a question?";
story[00].DestinationA = 02;
story[00].DestinationB = 03;
story[00].isHiddenA = false;
story[00].isHiddenB = false;

story[03] = new Object();
story[03].text = "Are you sure you don't want to ask the question? It might be an important one?";
story[03].DestinationA = 07;
story[03].DestinationB= 07;
story[03].isHiddenA = false;
story[03].isHiddenB = true;

story[02] = new Object();
story[02].text = "Johnny asked his mother: Mum, why are some of youre hairs turning grey? Do you want to see what his mother's response was?";
story[02].DestinationA = 04;
story[02].DestinationB = 06;
story[02].isHiddenA = false;
story[02].isHiddenB = false;

story[06] = new Object();
story[06].text = "Really, you had the courage to ask such an interesting question; now you dont want to see the responce!";
story[06].DestinationA = 07;
story[06].DestinationB = 07;
story[06].isHiddenA = false;
story[06].isHiddenB = true;

story[04] = new Object();
story[04].text = "The mother replied: Its because of you dear! Every bad action of your's will turn one of my hairs grey! Do you want to read what Johnny's reaction was?";
story[04].DestinationA = 05;
story[04].DestinationB = 01;
story[04].isHiddenA = false;
story[04].isHiddenB = false;

story[01] = new Object();
story[01].text = "Are you sure? Kid's do have funny responces?";
story[01].DestinationA = 07;
story[01].DestinationB = 07;
story[01].isHiddenA = false;
story[01].isHiddenB = true;

story[05] = new Object();
story[05].text = "Johnny replied, Now I know why grandmother has only grey hairs on her head! Haha...";
story[05].DestinationA = 07;
story[05].DestinationB= 07;
story[05].isHiddenA = false;
story[05].isHiddenB = true;

story[07]= new Object();
story[07].text= "Begin?";
story[07].DestinationA = 00;
story[07].DestinationB = 00;
story[07].isHiddenA = false;
story[07].isHiddenB = true;

// Choices for buttons //
 
story[00].buttonA = "Yes";
story[00].buttonB = "No";

story[01].buttonA = "Continue";
story[01].buttonB = "Continue.";

story[02].buttonA = "Yes";
story[02].buttonB = "No";
 
story[03].buttonA = "Continue";
story[03].buttonB = "Continue.";

story[04].buttonA = "Yes";
story[04].buttonB = "No";
 
story[05].buttonA = "Continue";
story[05].buttonB = "Continue.";
 
story[06].buttonA = "Continue";
story[06].buttonB = "Continue.";

story[07].buttonA = "Continue";
story[07].buttonB = "Continue";

// functions //

function OnPress(buttonPressed)
{
	if (buttonPressed === 'A')
	{
		page = story[page].DestinationA;
		document.getElementsByName('NavGameA')[00].value = story[page].buttonA;
		document.getElementsByName('NavGameB')[00].value = story[page].buttonB;
		document.getElementsByName('NavGameA')[00].hidden = story[page].isHiddenA;
		document.getElementsByName('NavGameB')[00].hidden = story[page].isHiddenB;
	}
	else if (buttonPressed === 'B')
	{
		page = story[page].DestinationB;
		document.getElementsByName('NavGameA')[00].value = story[page].buttonA;
		document.getElementsByName('NavGameB')[00].value = story[page].buttonB;
		document.getElementsByName('NavGameA')[00].hidden = story[page].isHiddenA;
		document.getElementsByName('NavGameB')[00].hidden = story[page].isHiddenB;
	}
	
	document.getElementById("story").innerHTML = story[page].text;
}