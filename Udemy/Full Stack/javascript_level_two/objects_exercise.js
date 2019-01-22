// Objects Exercise

////////////////////
// PROBLEM 1 //////
//////////////////

// Given the object below,
// Add a method called nameLength that prints out the
// length of the employees name to the console.

// My solution:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  nameLength: function() {
    console.log(this.name.length);
  }
}

// Instructor's solution:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  nameLength: function() {
    console.log(this.name.length);
  }
}


///////////////////
// PROBLEM 2 /////
/////////////////

// Given the object below,
// Write program that will create an Alert in the browser of each of the
// object's values for the key value pairs. For example, it should alert:

// Name is John Smith, Job is Programmer, Age is 31.

// My solution:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  bio: function() {
    alert("Name is " + this.name + ", job is " + this.job + ", age is " + this.age + ".")
  }
}

// Instructor Solution
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  bio: function() {
    alert("Name is " + this.name + ", job is " + this.job + ", age is " + this.age + ".")
  }
}


///////////////////
// PROBLEM 3 /////
/////////////////

// Given the object below,
// Add a method called lastName that prints
// out the employee's last name to the console.

// My solution:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  lastName: function() {
    nameArr = this.name.split(" ");
    console.log(nameArr[nameArr.length-1]);
  }
}

// Instructor's solution:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  lastName: function () {
    console.log(this.name.split(" ")[1]);
  }
}


// You will need to figure out how to split a string to an array.
// Hint: http://www.w3schools.com/jsref/jsref_split.asp
