// get players and player colors
var bluePlayer = prompt('Player 1 is Blue. Enter player 1\'s name.');
var bluePlayerColor = '#206fcf';

var redPlayer = prompt('Player 2 is Red. Enter player 2\'s name.');
var redPlayerColor = '#cf204e';

// set the game to true and grab the game board
var game_on = true;
var table = $('table tr');

// create function to change button color in table
function changeColor(rowIndex, colIndex, color) {
  return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color',color);
}

// create function to get existing color of button in table
function returnColor(rowIndex, colIndex) {
  return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color');
}

// create function to drop the color to the bottom of a column
function checkBottom(colIndex) {
  var colorReport = returnColor(5, colIndex);
  for (var row = 5; row > -1; row--) {
    colorReport = returnColor(row, colIndex);
    if (colorReport === 'rgb(218, 218, 218)') {
      return row
    }
  }
}

// #ffffff
// check for color matches
function colorMatchCheck(one, two, three, four) {
  return (one === two && one === three && one === four && one !== 'rgb(218, 218, 218)' && one !== undefined);
}

// check for wins
// horizonatal win
function horizontalWinCheck() {
  for (var row = 0; row < 6; row++) {
    for (var col = 0; col < 4; col++) {
      if (colorMatchCheck(returnColor(row, col), returnColor(row, col+1) ,returnColor(row, col+2), returnColor(row, col+3))) {
        console.log('Horizontal Win');
        return true;
      }else {
        continue;
      }
    }
  }
}

// vertical win
function verticalWinCheck() {
  for (var col = 0; col < 7; col++) {
    for (var row = 0; row < 3; row++) {
      if (colorMatchCheck(returnColor(row, col), returnColor(row+1, col) ,returnColor(row+2, col), returnColor(row+3, col))) {
        console.log('Vertical Win');
        return true;
      }else {
        continue;
      }
    }
  }
}

// diagonal win
function diagonalWinCheck() {
  for (var col = 0; col < 5; col++) {
    for (var row = 0; row < 7; row++) {
      if (colorMatchCheck(returnColor(row, col), returnColor(row+1, col+1) ,returnColor(row+2, col+2), returnColor(row+3, col+3))) {
        console.log('Diagonal Win');
        return true;
      }else if (colorMatchCheck(returnColor(row, col), returnColor(row-1, col+1) ,returnColor(row-2, col+2), returnColor(row-3, col+3))) {
        console.log('Diagonal Win');
        return true;
      }else {
        continue;
      }
    }
  }
}

// Game End
function gameEnd(winningPlayer) {
  for (var col = 0; col < 7; col++) {
    for (var row = 0; row < 7; row++) {
      $('#message').fadeOut('fast');
      $('h1').text(winningPlayer+" has won!");
      $('p').text('Refresh your browser to play again.');
    }
  }
}

// Start with Player One
var currentPlayer = 1;
var currentName = bluePlayer;
var currentColor = bluePlayerColor;

// Start with Player One
$('#message').text(bluePlayer + " choose a column to drop your color.");

$('.board button').on('click',function() {

  // Recognize what column was chosen
  var col = $(this).closest("td").index();

  // Get back bottom available row to change
  var bottomAvail = checkBottom(col);

  // Drop the chip in that column at the bottomAvail Row
  changeColor(bottomAvail, col, currentColor);

  // Check for a win or a tie.
  if (horizontalWinCheck() || verticalWinCheck() || diagonalWinCheck()) {
    gameEnd(currentName);
  }

  // If no win or tie, continue to next player
  currentPlayer = currentPlayer * -1 ;

  // Re-Check who the current Player is.
  if (currentPlayer === 1) {
    currentName = bluePlayer;
    $('#message').text(currentName +" it is your turn, please pick a column to drop your blue chip.");
    currentColor = bluePlayerColor;
  }else {
    currentName = redPlayer
    $('#message').text(currentName + " it is your turn, please pick a column to drop your red chip.");
    currentColor = redPlayerColor;
  }
})
