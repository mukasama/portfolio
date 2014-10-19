var	playersList = new Array(); //Create array//

function playrugby(){
'use strict';  //Retrieving all values//
var playerfirstname = document.getElementById('playerfirstname').value; 
var playersecondname = document.getElementById('playersecondname').value;
var email = document.getElementById('email').value;
var rugbypositions = document.getElementById('rugbypositions').value;
var tableID = document.getElementById('tableID');
var players = {
playerfirstname: playerfirstname,
playersecondname: playersecondname,
email: email,
rugbypositions: rugbypositions,
joinDate: new Date()
};
if (players.playerfirstname && players.playersecondname){
playersList.push(players);
}
var count = playersList.length;
for (var i = count-1; i < count; i++){
tableID.innerHTML += playersList[i].playerfirstname + '\t\t' + playersList[i].playersecondname + '\t\t' + playersList[i].email + '\t\t' + playersList[i].rugbypositions + '\t\t' + playersList[i].joinDate.toLocaleString() + '\n' + "<br>";
}
return false;
}
function init(){
'use strict';
document.getElementById('game').onsubmit = playrugby; //calling the function//
}
window.onload = init; 