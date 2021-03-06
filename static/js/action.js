// Global variables
const task_title = document.querySelector('#tTitle');
const task_desc = document.querySelector('#tTextarea');

const error_title = document.querySelector('#titleErr');
const error_desc = document.querySelector('#descErr');

const clearBtn = document.querySelector('#form-clearBtn');

let alertBar = document.querySelector('#alertBar');


// Function: Clear fields under New Task
function clrUserInputs(e) {
    
    task_title.value = "";
    task_desc.value = "";
    error_title.innerHTML = "";
    error_desc.innerHTML = "";

    e.preventDefault();
};

// Toggle between error messages of validateForm()
function printError(elemId, hintMsg) {
    document.getElementById(elemId).innerHTML = hintMsg;
}

// Validate user form
function validateForm(e) {

    // Retrieve title and description value
    let title = document.taskForm.title.value;
    let description = document.taskForm.description.value;

    // Set title and description error flag to determine,
    // true = error exist, false = error remove
    let titleErr = descErr = true;

    if (title==="") {        
        printError("titleErr", "Please insert title.");
    } else {
        titleErr = false;
        printError("titleErr", "");
    }

    if (description==="") {        
        printError("descErr", "Please insert descriptions.");
    } else {
        descErr = false;
        printError("descErr", "");
    }

    // Return false to prevent form POST when conditions above does met
    if ((titleErr || descErr) == true) {
        return false;
    }

};

function removeFadeOut(el, speed) {
    
    var seconds = speed/1000;
    el.style.transition = "opacity "+seconds+"s ease";
    el.style.opacity = 0;

    setTimeout(function() {
        el.parentNode.removeChild(el);
    }, speed);
}

// Execute when document is ready
document.addEventListener('DOMContentLoaded', function(e){

    if (alertBar) {
        removeFadeOut(alertBar, 7000);            
    }

    clearBtn.addEventListener('click', clrUserInputs);
});