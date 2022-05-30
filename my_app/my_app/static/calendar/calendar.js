const today = new Date();
let currentMonth = today.getMonth();
let currentYear = today.getFullYear();
let events = {
    "PROJECT_NAME": "NAME",
    "PROJECT_KEY": "KEY",
    "Schedule": { 
    }
}
function onClick() {
    let nextButton = document.querySelector("#nextMonth");
    let previousButton = document.querySelector("#previousMonth");
  
    nextButton.addEventListener("click", nextMonth);
    previousButton.addEventListener("click", previousMonth);

}
  
function previousMonth() {
    if (currentMonth === 0) {
        currentYear = currentYear - 1;
        currentMonth = 11;
        showCalendar(currentMonth, currentYear);
    }
    else {
        currentYear = currentYear;
        currentMonth = currentMonth - 1;
        showCalendar(currentMonth, currentYear);
    }
}
function nextMonth() {
    if (currentMonth === 11) {
        currentYear = currentYear + 1;
        currentMonth = (currentMonth + 1) % 12;
        showCalendar(currentMonth, currentYear);
    }
    else {
        currentYear = currentYear;
        currentMonth = (currentMonth + 1) % 12;
        showCalendar(currentMonth, currentYear);
    }
}

function scrapeCalendar(index) {
    fetch("http://127.0.0.1:8000/jira/issues")
    .then((response) => response.json())
    .then((data) => {
      //grabs data from index
      events = data.schedule.Projects[Number(`${index}`)];
    });
}


function showCalendar(month, year) {

    let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    let firstDay = (new Date(year, month)).getDay();
    let daysInMonth = 32 - new Date(year, month, 32).getDate();

    let tbl = document.getElementById("calendar-body");

    // clear previous cells
    tbl.innerHTML = "";

    monthYear.innerHTML = months[month] + " " + year;

    // create cells
    let date = 1;
    for (let rowNum = 0; rowNum < 6; rowNum++) {
        let row = document.createElement("tr");
        for (let columnNum = 0; columnNum < 7; columnNum++) {
            if (date > daysInMonth) {
                if (rowNum < 5) {
                    tbl.appendChild(row);
                    row = document.createElement("tr");
                    row.setAttribute('style', "border:none;");
                    rowNum++;
                }
                break;
            }
            let cell = document.createElement("td");
            if (rowNum === 0 && columnNum < firstDay) {
                let cellText = document.createTextNode("");
                cell.appendChild(cellText);
                row.appendChild(cell);
            }
            else {
                let cellText = document.createTextNode(date);
                cell.appendChild(cellText);

                let dateObject = new Date(year,month,date);
                let dateString = dateObject.toLocaleDateString('en-CA'); // YYYY-MM-DD
                let dailyEvents = [] 
                Object.keys(events.Schedule).forEach( key => {
                    if (events.Schedule[key] === dateString) dailyEvents.push(key);
                })

                //console.log(dailyEvents);
                dailyEvents.every( event => {
                    let ul = document.createElement('ul');
                    let li = document.createElement("li");
                    li.innerHTML=event;
                    ul.appendChild(li);
                    cell.appendChild(ul);	

                    // color events before today in green and events after today in gray
                    cell.style.backgroundColor = (dateObject < today) ? "green" : "Orange";
                    return false; // only display one event per day for now
                })

                if (date === today.getDate() && month === today.getMonth() && year === today.getFullYear()) {
                    cell.classList.add("bg-light"); // color today's date in gray
                }

                row.appendChild(cell);
                date++;
            }
        }
        tbl.appendChild(row);
    }
}


//ensure functions run sequentially
function a(index) {
    return new Promise(function (resolve) {
      setTimeout(function () {
        scrapeCalendar(index);
        resolve();
      }, 50);
    });
  }

  function b() {
    return new Promise(function (resolve) {
      setTimeout(function () {
        currentMonth = today.getMonth();
        currentYear = today.getFullYear();
        showCalendar(currentMonth, currentYear);
        resolve();
      }, 50);
    });
  }

  function c() {
    return new Promise(function (resolve) {
      setTimeout(function () {
        onClick();
        resolve();
      }, 50);
    });
  }

//calls promised based functions
export function calendarFunction(index){
    a(index)
      .then(b)
      .then(c)
    }
    
//initialize calendar
b()
.then(c)