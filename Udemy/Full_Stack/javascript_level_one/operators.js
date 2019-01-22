
// booleans - always lowercase is js
true
false

///////////////////////////
// Comparison Operators //
/////////////////////////

// greater than
3 > 2;  // true
2 > 3;  // false

// less than
1 < 2;

// greater than or equal to
2 >= 1;

// less than or equal to
1 <= 2;

// equality
2 == 2;             // true
"user" == "user";   // true

// inequality
2 != 3;

// BUT WAIT! When we compare a number to a string...
2 == "2"  // true

// JS uses type coercion! This means it will try it's best to convert objects
// to similar data types to perform the comparison! A lot of times you don't
// actually want that!

// We want a way to check equality of both value AND type!
// Add another set of equals signs to do this!

// check equality for BOTH value and type
5 === 5   // true
5 === "5" // false

// check for inequality for BOTH value and type
5 !== 5    // false
5 !== "5"  // true

// many programming languages also use 0 and 1 to represent true and false
// it's the same for javascript, but the type doesn't match

true == 1;  // true
true === 1; // false

false == 0;   // true
false === 0;  // false

// then theres the weird behavior for null, undefined and NaN values

null == undefined; // true
Nan == Nan; // false

////////////////////////
// Logical Operators //
//////////////////////

// Logical Operators allow us to combine multiple comparison Operators

// AND is written with &&
// both conditions must be true to return true
1 === 1 && 2 === 2

// OR is written with ||
// one or the other conditions must be true to return true
1 === 2 || 2 === 2

// NOT is written with !
// a way of checking if the oposite of a condition is true
!(1 === 1);


// EXERCISES
var x = 1
var y = 2

// Exercise 1
"2" == y && x === 1;  // true

// Exercise 2
x >= 0 || y === "2";  // true

// Exercise 3
!(x !== 1) && y === (1+1);  //true

// Exercise 4
y !== "2" && x < 10;  // true

// Exercise 5
y !== x || y == "2" || x === 3; //true
