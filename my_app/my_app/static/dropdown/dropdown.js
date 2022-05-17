import * as timeline from "/static/timeline/timeline.js"



//function onclick
function onClick(){
    let startButton = document.querySelectorAll(".dropdown-item")
  
      startButton.forEach(function(check){
        check.addEventListener('click', checkIndex);
      })
  
      function checkIndex(event){
        let idx = Array.from(startButton).indexOf(event.target)
        //add more calendar function below
        timeline.timelineFunction(idx)
      }
  }

//calls onclick
onClick()
