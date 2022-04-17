
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


const theDiv = document.getElementById("input-flex-container");
const div = document.createElement('div');
div.className = "input";
div.innerHTML += `<span data-year="120" data-info="End date"></span>`;
theDiv.append(div);


