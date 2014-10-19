// JavaScript Document
var story = [];
var i =0;

story[0] = "As Johnny's mother had just come back from work, seating in the living room.";
story[1] = "Johnny asked his mother: Mum, why are some of your hairs turning grey?";
story[2] = "The mother tried to use this occasion to teach her child: “It is because of you, dear.";
story[3] = "Every bad action of yours will turn one of my hairs grey!";
story[4] = "The child replied innocently: Now I know why grandmother has only grey hairs on her head.";
story[5] = "Hahaha...THE END!";

function OnPress()
{
    document.getElementById("story").innerHTML = story[i];
	i++;
	if(i ===6){i=0;}
}