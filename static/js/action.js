// Global variables
const task_title = document.querySelector('#tTitle');
const task_desc = document.querySelector('#tTextarea');
const submitBtn = document.querySelector('#form-submitBtn');
const clearBtn = document.querySelector('#form-clearBtn');


// Function: Clear fields under New Task
function clrUserInputs() {
    
    task_title.value = "";
    task_desc.value = "";
    
};

// Function: Check if inputs are blank
function checkForBlanks() {

    console.log(task_title.value + " " + task_desc.value);

}

function forValidation() {

}

// Execute when document is ready
document.addEventListener('DOMContentLoaded', function(e){
    
    clearBtn.addEventListener('click', clrUserInputs);
    // submitBtn.addEventListener('submit', checkForBlanks);

    e.preventDefault();

});