//implementation to change color
function changeCircleColor() {
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
    Dec: 12,
  };
  Object.freeze(enum_Months);


  //todays date
  let dateMillSeconds = Date.now();
  let date = new Date(dateMillSeconds);
  let todaysDate =
    date.getMonth() + 1 + " " + date.getDate() + " " + date.getFullYear();


  //date extracted from 4g timeline + target color change
  const theDiv = document.getElementById("input-flex-container");
  for (let i = 0; i < theDiv.children.length; i++) {
    //extract data from each milestone on the timeline into a substring
    let j = theDiv.getElementsByClassName("input")[i].innerHTML;
    let timelineDate = j.substring(
      j.indexOf("=") + 2,
      j.lastIndexOf("data") - 2
    );

    //array of strings
    let timelineSplit = timelineDate.split(" ");
    let todaySplit = todaysDate.split(" ");

    //get rid of leading zeros, change string date to num representation
    if (timelineSplit != "None") {
      let temp1 = timelineSplit[1];
      temp1 = parseInt(temp1, 10);
      timelineSplit[1] = String(temp1);

      let temp2 = enum_Months[timelineSplit[0]];
      timelineSplit[0] = String(temp2);
    }

    //change color based on comparisons on date
    if (timelineSplit != "None") {
      if (parseInt(todaySplit[2]) > parseInt(timelineSplit[2])) {
        (theDiv.getElementsByClassName("input")[
          i
        ].style.backgroundColor = "green");
      } else if (
        parseInt(todaySplit[2]) >= parseInt(timelineSplit[2]) &&
        parseInt(todaySplit[0]) > parseInt(timelineSplit[0])
      ) {
        (theDiv.getElementsByClassName("input")[
          i
        ].style.backgroundColor = "green");
      } else if (
        parseInt(todaySplit[2]) >= parseInt(timelineSplit[2]) &&
        parseInt(todaySplit[0]) >= parseInt(timelineSplit[0]) &&
        parseInt(todaySplit[1]) >  parseInt(timelineSplit[1])
      ) {
        (theDiv.getElementsByClassName("input")[
          i
        ].style.backgroundColor = "green");
      }
      else{
        (theDiv.getElementsByClassName("input")[
          i
        ].style.backgroundColor = "Gray");
      }
    }
    else{
      (theDiv.getElementsByClassName("input")[
        i
      ].style.backgroundColor = "DarkBlue");
    }
  }
}

//replaces dates with values from schedule file
function timelineScrape(index) {
  let arr = [];

  //enum for months
  const enum_Months = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "June",
    7: "July",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec",
  };
  Object.freeze(enum_Months);

  fetch("http://127.0.0.1:8000/jira/issues")
    .then((response) => response.json())
    .then((data) => {
      //grabs data from index
      arr = data.schedule.Projects[Number(`${index}`)].Schedule;

      const theContainer = document.getElementById("input-flex-container");
      for (let i = 0; i < theContainer.children.length; i++) {
        let theMilestone = theContainer.getElementsByClassName("input")[i]

        //If the date is "null", set to "none". Else fix the incoming date format
        let tempYearData = String(Object.values(arr)[i]);
        if (tempYearData === "null") {
          tempYearData = "None";
        } else {
          tempYearData = tempYearData.replace(/-/g, " ");
          let tempYearSplit = tempYearData.split(" ");
          let month = tempYearSplit[1];
          month = parseInt(month, 10);
          month = enum_Months[month];
          tempYearData =
            month + " " + tempYearSplit[2] + " " + tempYearSplit[0];
          //console.log(tempYearData)
        }

       
        theMilestone.getElementsByTagName('span')[0].outerHTML = `<span data-year="${tempYearData}" data-info="${Object.keys(arr)[i]}"></span>`
      }
    });
}

//changes color of the line 
function changeLineColor(){
  //rgbToHex (copied function)
  const rgb2hex = (rgb) => `#${rgb.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/).slice(1).map(n => parseInt(n, 10).toString(16).padStart(2, '0')).join('')}`

  const theContainer = document.getElementById("input-flex-container");
  for (let i = 0; i < theContainer.children.length; i++) {

    const lineBefore = document.getElementById(`before${i+1}`)
    const lineAfter = document.getElementById(`after${i+1}`)

    const circle = theContainer.getElementsByClassName("input")[i]
    const circleColor = rgb2hex(window.getComputedStyle(circle).getPropertyValue(('background-color')))
    
    lineBefore.style.backgroundColor = `${circleColor}`
    lineAfter.style.backgroundColor = `${circleColor}`


  }
}

//ensure functions run sequentially
function a(index) {
  return new Promise(function (resolve) {
    setTimeout(function () {
      timelineScrape(index);
      resolve();
    }, 50);
  });
}

function b() {
  return new Promise(function (resolve) {
    setTimeout(function () {
      changeCircleColor();
      resolve();
    }, 50);
  });
}

function c() {
  return new Promise(function (resolve) {
    setTimeout(function () {
      changeLineColor();
      resolve();
    }, 50);
  });
}





//calls promised based functions
export function timelineFunction(index){
a(index)
  .then(b)
  .then(c)
}





  