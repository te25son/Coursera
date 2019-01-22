// ARRAYS

var countries = [
  "USA",
  "Germany",
  "China"
]

// access elements of an array
// first country from countries
countries[0]

// second country from countries
countries[1]

// third country from countries
countries[2]

// reassign items in an array
countries[2] = "Italy"

// immutable - cannot be changed (e.g. string)
// mutable - can be changed (e.g. array)

// Arrays can hold multiple different data types
// for example...
mixedArray = [true, "Da Bears!", 50]

// get length of an array (returns how many elements are in an array)
mixedArray.length

myArr = ["one", "two", "three"]

// adding elements to an array using .push()
myArr.push("four")

// remove elements from an array using .pop()
myArr.pop()

// index the last item in an array using .length
myArr[myArr.length - 1]

// nested arrays
var matrix = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
matrix.length // 3
matrix[0].length // 3

// iterate over arrays
var arr = ["a", "b", "c"]
for (var i = 0; i < arr.length; i++) {
  console.log(arr[i])
}

for (element of arr) {
  console.log(element);
}

// you can do the same with the forEach method
arr.forEach(alert)

function isAwesome (name) {
  console.log(name + " is awesome");
}

var topics = ["Python", "Django", "Javascript"]

topics.forEach(isAwesome)
