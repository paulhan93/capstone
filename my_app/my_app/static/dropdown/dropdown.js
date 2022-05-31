import * as calendar from "/static/calendar/calendar.js";
import * as timeline from "/static/timeline/timeline.js";

//checks which entry was clicked and returns the appropriate index
function onClick() {
  let startButton = document.querySelectorAll(".dropdown-item");

  startButton.forEach(function (check) {
    check.addEventListener("click", checkIndex);
  });

  function checkIndex(event) {
    let index = Array.from(startButton).indexOf(event.target);
    let name = Array.from(startButton)[index].innerHTML
    changeTitle(name)
    calendar.calendarFunction(index);
    timeline.timelineFunction(index);
  }
}

//changes title according to selected name
function changeTitle(name){
       //change title based on clicked name
        const title = document.getElementsByTagName("h2")[0]
        title.innerHTML = name;
}

//populates entries in the menu according to the issues page
function populateMenu(){
    fetch("http://127.0.0.1:8000/jira/issues")
    .then((response) => response.json())
    .then((data) => {
        //grabs issue names and inserts into menu
        const dropDown = document.getElementsByClassName("dropdown-menu")[0]
        const names = data.schedule.Projects
        for(let i = 0; i < names.length; i++){
            var name = Object.values(names[i])[0]
           
            let tag = document.createElement("a");
            tag.classList.add("dropdown-item")
            tag.href = "#"
            tag.innerHTML = name
            //console.log(tag)

            dropDown.appendChild(tag);
        }
    });
}



//ensure functions run sequentially
function a() {
    return new Promise(function (resolve) {
      setTimeout(function () {
        populateMenu();
        resolve();
      }, 50);
    });
  }

  function b() {
    return new Promise(function (resolve) {
      setTimeout(function () {
        onClick();
        resolve();
      }, 50);
    });
  }

//calls the promise based functions
  a()
  .then(b)