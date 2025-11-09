// Get the value of the name input from the form and update the greeting

const API = "http://127.0.0.1:5000/Gemini_Request";
const content1 = document.querySelector("#content1"); // get greeting element
const inputElement1 = document.querySelector("#exampleFormControlInput1"); // get input element
const btn = document.querySelector("#exampleFormBtn1"); // get the element with id = 'exampleFormBtn'

btn.addEventListener("click", function () {
    if(isNaN(Number(inputElement1.value))){
        return ;
    }
    content1.innerHTML = `$ ${inputElement1.value}`; 
});
const content2 = document.querySelector("#content2"); // get greeting element
const inputElement2 = document.querySelector("#exampleFormControlInput2"); // get input element
const btn2 = document.querySelector("#exampleFormBtn2"); // get the element with id = 'exampleFormBtn'
btn2.addEventListener("click", function () {
    if(isNaN(Number(inputElement2.value))){
        return ;
    }
    // add an event to the button: whenever the button is pressed, update the greeting name
    content2.innerHTML = `$ ${inputElement2.value}`; 
    // this is a templated string in JavaScript! https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals
});
let sum_expenses = 0 
const content3 = document.querySelector("#content3"); // get greeting element

function submitNumber(inputId, outputId) {
    const value = document.getElementById(inputId).value;
    if (!value){
        return ;
    }
    document.getElementById(outputId).innerText = value ? `$${value}` : "No expenses yet.";
    update_sum(value)
};

let savingsGoal = 0;

function submitGoal() {
    const input = document.getElementById("savings-goal").value;
    savingsGoal = input ? Number(input) : 0;
    document.getElementById("goal-display").innerText = 
        savingsGoal ? `$${savingsGoal}` : "No goal set yet.";
}

function update_sum(value) {
    sum_expenses+= Number(value)
    content3.innerHTML = `$ ${sum_expenses}`;
}