var first = prompt("Enter your first name:")
var last = prompt("Enter your last name:")
var age = prompt("Enter your age:")
var height = prompt("Enter your height in centimeters:")
var pet = prompt("Enter your pet's name:")

if (
  (first[0] === last[0]) && (age > 20 && age < 30) && (height >= 170) && (pet[pet.length-1] === "y")
) {
  console.log("Welcome Brother!");
}
