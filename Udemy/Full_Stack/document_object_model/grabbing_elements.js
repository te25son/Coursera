// DOM (document object model)

// Grabbing elements from the document model

// important document attributes:
document.URL  // grabs the document URL
document.body  // grabs the documents HTML body
document.links  // grabs the document HTML links
document.head // grabs the document HTML head

// methods for grabing specific elemtents from the DOM
document.getElementById()  // returns an element with whatever ID you pass in
document.getElementsByClassName()  // returns a list of all items belonging to the given class
document.getElementsByTagName()  // returns a list of all elements with a certain tag
document.querySelector()  // returns the first object containing the css style selector
document.querySelectorAll()  // returns all objects containing the css style selector

// example of how to get an element and set it to a variable
var myVariable = document.querySelector('p')

// other useful ways of grabbing elements and groups of elements
myVariable.textContent  // returns just the text
myVariable.innerHTML  // returns the text with any html tags
myVariable.getAttribute()  // returns the the original attribute
myVariable.setAttribute()  // allows you to set an attribute
