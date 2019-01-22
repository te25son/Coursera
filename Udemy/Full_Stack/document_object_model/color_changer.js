// grab the header with h1
// var header = document.querySelector('h1')

var element_g1 = document.querySelector('#g1')
var element_o = document.querySelector('#o')
var element_i = document.querySelector('#i')
var element_n = document.querySelector('#n')
var element_g2 = document.querySelector('#g2')
var element_c = document.querySelector('#c')
var element_r = document.querySelector('#r')
var element_a1 = document.querySelector('#a1')
var element_a2 = document.querySelector('#a2')
var element_a3 = document.querySelector('#a3')
var element_z = document.querySelector('#z')
var element_y = document.querySelector('#y')
var element_exc = document.querySelector('#exc')



// interface the object with the style
// header.style.color = 'red';

element_g1.style.color = 'red';
element_o.style.color = 'red';
element_i.style.color = 'red';
element_n.style.color = 'red';
element_g2.style.color = 'red';
element_c.style.color = 'red';
element_r.style.color = 'red';
element_a1.style.color = 'red';
element_a2.style.color = 'red';
element_a3.style.color = 'red';
element_z.style.color = 'red';
element_y.style.color = 'red';
element_exc.style.color = 'red';

// create a random color function
function getRandomColor() {
  var chars = '0123456789ABCDEF';
  var color = '#'
  for (var i = 0; i < 6; i++) {
    color += chars[Math.floor(Math.random()*16)]
  }
  return color
}

// simple function for clarity
function changeElement1Color() {
  colorInput = getRandomColor();
  element_g1.style.color = colorInput;
}
function changeElement2Color() {
  colorInput = getRandomColor();
  element_o.style.color = colorInput;
}
function changeElement3Color() {
  colorInput = getRandomColor();
  element_i.style.color = colorInput;
}
function changeElement4Color() {
  colorInput = getRandomColor();
  element_n.style.color = colorInput;
}
function changeElement5Color() {
  colorInput = getRandomColor();
  element_g2.style.color = colorInput;
}
function changeElement6Color() {
  colorInput = getRandomColor();
  element_c.style.color = colorInput;
}
function changeElement7Color() {
  colorInput = getRandomColor();
  element_r.style.color = colorInput;
}
function changeElement8Color() {
  colorInput = getRandomColor();
  element_a1.style.color = colorInput;
}
function changeElement9Color() {
  colorInput = getRandomColor();
  element_a2.style.color = colorInput;
}
function changeElement10Color() {
  colorInput = getRandomColor();
  element_a3.style.color = colorInput;
}
function changeElement11Color() {
  colorInput = getRandomColor();
  element_z.style.color = colorInput;
}
function changeElement12Color() {
  colorInput = getRandomColor();
  element_y.style.color = colorInput;
}
function changeElement13Color() {
  colorInput = getRandomColor();
  element_exc.style.color = colorInput;
}

// perform the action over intervals (milliseconds)
setInterval("changeElement1Color()", 50);
setInterval("changeElement2Color()", 50);
setInterval("changeElement3Color()", 50);
setInterval("changeElement4Color()", 50);
setInterval("changeElement5Color()", 50);
setInterval("changeElement6Color()", 50);
setInterval("changeElement7Color()", 50);
setInterval("changeElement8Color()", 50);
setInterval("changeElement9Color()", 50);
setInterval("changeElement10Color()", 50);
setInterval("changeElement11Color()", 50);
setInterval("changeElement12Color()", 50);
setInterval("changeElement13Color()", 50);
