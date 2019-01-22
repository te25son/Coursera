// for loops in javascript

// for - loops through a number of times
// example

for (statement1; statement2; statement3) {
  // execute some code
}

// statement1 is executed before the loop starts
// statement2 defines the condition for running the loop
// statement3 is executed each time after the loop cycles through

for (var i = 0; i < array.length; i++) {
  array[i]
}

var abet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for (var i = 0; i < abet.length; i++) {
  console.log(abet[i]);
}

// for/in loops through a js object

for (var variable in object) {
  if (object.hasOwnProperty(variable)) {

  }
}

// for/of used with arrays

for (variable of iterable) {

}

// multiple ways of writing num = num + 1

var num = 1
num = num + 1
num += 1
num ++
