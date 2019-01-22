// event handling with jQuery
// select the first h1 element in your html file
var firstText = $('h1').eq(0).text()
var firstH1 = $('h1').eq(0)

firstH1.hover(
  function() {
    $(this).text('You found the secret!');
  }, function() {
    $(this).text(firstText);
  }

)

// key press
// keep track of which key is pressed
$('input').eq(1).keypress(
  // use the parameter event to get an object back and find out which button was pressed
  function(event) {
    $('h1').toggleClass('turnBlue');
    // display the returned object to the console
    console.log(event);
  }
)

// make a new function to handle only certain key presses
$('input').eq(0).keypress(
  function(event) {
    // 13 is the space bar
    if (event.which === 13) {
      $('h1').toggleClass('turnRed');
    }
  }
)

// on() - sort of like addEventListener
firstH1.on('mouseover', function() {
  $(this).text('You found the big secret!');
})

// jquery animations
$('input').eq(2).on('click', function() {
  $('.container').fadeOut(3000);
})
