// FUNCTIONS
// javascript syntax for a funtion
function functionName(parameter1, parameter2) {
  // code to be executed
}

// simple function
function helloHuman (name) {
  console.log("Hello " + name);
}


function addNum(num1, num2) {
  console.log(num1 + num2);
}

// assign default values
function helloSomeone(name = "whachamanames") {
  console.log("Hello " + name);
}

// return values instead of printing to console
function formal(name = "Samuel", title = "Sir") {
  return title + " " + name
}


function timesFive(num) {
  // LOCAL SCOPE to the function
  // variables defined within a function are local to that function,
  // i.e. they do not exist outside of that function
  var result = num * 5
  return result
}

// GLOBAL SCOPE
// variables that exist outside of functions
