// use $ to grab items from the DOM
// get the h1 element
$('h1')

// get all the li elements
$('li')

// get all elements with container class
$('.container')

// get all elements with the id special
$('#special')

// if multiple items with the same element exist, jquery will return a list of those items
// you can select individual items if you know where they are in the list
var listItem0 = $('li')[0]
var listItem1 = $('li')[1]
...
// the more common and less buggy method (aka the preferred method) is to use .eg(//the number of item you want)
var listItems = $('li')
listItems.eq(1).methodYouWant()

// you can get the last element in a list by using negative indexing
listItems.eq(-1)

// you can change an elements css using jquery
var x = $('h1')
x.css('color', 'white')  // first parameter = the element you want to change, second element = what you want to change the element to
x.css('background', 'blue')

// you can change mulitple css properties at once by passing an object
// create the object
var newCSS = {
  'color', 'white',
  'background': 'silver',
  'border': '5px solid red',
}
// pass the object into jquery function
x.css(newCSS)

// grabbing text with jquery
$('h1').text()

// changing the text with jquery
$('h1').text('New text goes here and replaces old text.')

// grabbing html with jquery
$('h1').html()

// changing html with jquery
$('h1').html('<em>chaning stuff!</em>')

// changing input tags
// change the type of input
$('input').eq(0).attr('type', 'checkbox')  // first parameter = the element you want to change, second element = what you want to change the element to

// change the value of the input
$('input').eq(0).val('new value')

// add an existing class with jquery
$('h1').addClass('turnRed')

// remove a class with jquery
$('h1').removeClass('turnRed')

// toggle a class (remove if there, add if not)
$('h1').toggleClass('turnBlue')
