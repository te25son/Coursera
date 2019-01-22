// conditionals in javascript

if (condition_one){
  "do something"
}else{
  "do something else"
}

// or with more conditions

if (condition_one){
  "do something"
}else if (condition_two){
  "do something else"
}else{
  "do something else"
}


// examples

var hot = false
var temp = 60

if (temp > 80) {
  console.log("It's hot");
} else {
  console.log("It's not very hot today");
}

if (temp>80) {
  console.log('it\'s hot outside');
} else if (temp<=80 && temp>=50) {
  console.log('it\'s not so bad outside');
} else if (temp<50 && temp>=32) {
  console.log('it\'s pretty cold outside');
} else {
  console.log('it\'s freaking cold outside');
}


var coffee = 10;
var tea = 10;
var report = "blank";

if (coffee >= 10 && tea >= 10) {
  report = "strong sales of both coffee and tea"
} else if (coffee === 0 && tea = == 0) {
  report = "nothing sold"
} else if (coffee >= 10 && tea < 10) {
  report = "we had strong sales of coffee, but weak sales of tea"
} else if (coffee < 10 && tea >= 10) {
  report = "we had strong sales of tea, but weak sales of coffee"
} else {
  report = "we had average sales of both coffee and tea"
}

console.log(report);
