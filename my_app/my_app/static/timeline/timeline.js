//code to create new elements upon button press
let btn = document.getElementById("btn");
btn.addEventListener('click', event => {
    for (let i = 0; i < 3; i++) {
    const theDiv = document.getElementById("input-flex-container");
    const div = document.createElement('div');
    div.className = "input";
    div.innerHTML += `<span data-year="120" data-info="End date"></span>`;
    theDiv.append(div);
    }
});


/*
//general code for inserting once script loads
const theDiv = document.getElementById("input-flex-container");
const div = document.createElement('div');
div.className = "input";
var text1 = "BBB date";
div.innerHTML += `<span data-year="120" data-info="${text1}"></span>`;
theDiv.append(div);
*/



//implementation to change color
const enum_Months = {
  Jan: 1,
  Feb: 2,
  Mar: 3,
  Apr: 4,
  May: 5,
  June: 6,
  July: 7,
  Aug: 8,
  Sep: 9,
  Oct: 10,
  Nov: 11,
  Dec: 12
};
Object.freeze(enum_Months);
//let month= enum_Months.Dec;
//console.log(month);


//todays date
var dateMillSeconds = Date.now();
var date = new Date(dateMillSeconds);
var todaysDate = date.getMonth()+1 + ' ' + date.getDate() + ' ' + date.getFullYear();
console.log(todaysDate);

//date extracted from 4g timeline + target color change
var theDiv = document.getElementById("input-flex-container");
for(let i = 0; i < theDiv.children.length; i++){
  //extract data from each milestone on the timeline into a substring
  let j = theDiv.getElementsByClassName("input")[i].innerHTML;
  var timelineDate = j.substring(
    j.indexOf("=") + 2, 
    j.lastIndexOf("data") - 2
  );

  //array of strings
  var timelineSplit = timelineDate.split(' ');
  var todaySplit = todaysDate.split(' ');


  //get rid of leading zeros, change string date to num representation
  if(timelineSplit != "None"){
  let temp1 = timelineSplit[1];
  temp1 = parseInt(temp1, 10);
  timelineSplit[1] = String(temp1);

  let temp2 = enum_Months[timelineSplit[0]];
  timelineSplit[0] = String(temp2);
  }
  //console.log(timelineSplit);
  //console.log(todaySplit);

  //change color based on comparisons on date
  if(timelineSplit != "None"){
    if(todaySplit[2] > timelineSplit[2]){
      let k = theDiv.getElementsByClassName("input")[i].style.backgroundColor = "green";
    }
    else if((todaySplit[2] >= timelineSplit[2]) && (todaySplit[0] > timelineSplit[0])){
      let k = theDiv.getElementsByClassName("input")[i].style.backgroundColor = "green";
    }
    else if ((todaySplit[2] >= timelineSplit[2]) && (todaySplit[0] >= timelineSplit[0]) && (todaySplit[1] > timelineSplit[1])){
      let k = theDiv.getElementsByClassName("input")[i].style.backgroundColor = "green";
    }
  }



  
}






fetch('http://127.0.0.1:8000/jira/test')
  .then(response => response.json())
  .then(data => {
      console.log(data)
      //console.log(data.schedule[0])
    });

