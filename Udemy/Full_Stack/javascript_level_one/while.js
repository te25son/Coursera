// while loop will continuously run code as long the condition remains true

// syntax
while (true) {
  // execute some conde
  // while this is true
}

 var x = 0;

 while (x < 5) {
   console.log('x is: ' + x);
   console.log('x is still less than 5, adding 1 to x...');
   x = x ** 2
 }

 var x = 0;

 while (x < 5) {
   console.log('x is: ' + x);
   if (x === 3) {
     console.log('x is EQUAL to 3');
     break;
   }
   console.log('x is still less than 5, adding 1 to x...');
   x = x + 1
 }

 // age example
 var age = prompt('What\'s your age?')
 var guess = 0

 while (age >= guess) {

     console.log("Are you " + guess + "?");

   if (guess == age) {
     console.log("I got it! You're " + guess);
     break;
   }

   console.log("No? Let me guess again...");
   guess = guess + 1
 }

 // while loop 1 - 10
var x = 1
while (x < 11) {
  if (x % 2 === 0) {
    console.log(x);
  }
  x = x + 1;
}
