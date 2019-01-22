// find info on events here
// https://developer.mozilla.org/en-US/docs/Web/Events

// 'listen' for an event
// myVariable.addEventListener(event, funct);

// example...
// var head.querySelector('h1');
// head.addEventListener('click', changeColor);

// run some real examples
var headHover = document.querySelector('#hover')
var pDoubleClick = document.querySelector('#doubleClick')
var pClick = document.querySelector('#click')

// add an event listener
headHover.addEventListener('mouseover', function() {
  headHover.textContent = 'Do you believe in Magic?';
  headHover.style.color = 'red';
})

// notice that this will change the text and color permanently
// if you want to only change the text and color while hovering, do this...
headHover.addEventListener('mouseout', function() {
  headHover.textContent = 'Some More Examples';
  headHover.style.color = 'black';
})

// add a click
pClick.addEventListener('click', function(){
  pClick.innerHTML = '<strong>A secret hidden in the internet!</strong>';
  pClick.style.color = 'aqua'
})

// add a double click
pDoubleClick.addEventListener('dblclick', function(){
  pDoubleClick.innerHTML = '<em>So MaNy SeCrEtS oN tHe InTeRnEt!!!!</em>';
  pDoubleClick.style.color = 'green';
})
