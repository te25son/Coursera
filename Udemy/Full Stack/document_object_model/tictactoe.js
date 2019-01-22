// define all game variables...
// start button:
var start = document.querySelector('#start')
var game = document.querySelector('#game')
// grab table cells
var cells = document.querySelectorAll('td')
// click count for play function
var clickCount = 0

// add event listener and function for game start
// event listener
start.addEventListener('click', gameStart)
// function
function gameStart() {
  alert("The game has started. X goes first.");
  game.style.visibility = 'visible';
}

// give function play() to all cells with for loop
for (var i = 0; i < cells.length; i++) {
  cells[i].addEventListener('click', play)
}

// add play function
function play() {
  if (this.textContent === '') {
    if (clickCount % 2 == 0) {
      this.textContent = 'X';
      this.style.background = '#5f5f5f';
      this.style.color = "white";
      clickCount++
    } else {
      this.textContent = 'O';
      this.style.background = '#5f5f5f';
      this.style.color = "white";
      clickCount++
    }
  } else {
    alert('Square already taken. Choose another.')
  }
}
