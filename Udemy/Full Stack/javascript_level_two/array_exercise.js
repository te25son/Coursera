var roster = []

function addNew(name) {
  var name = prompt("What name would you like to add to the roster?")
  if (roster.includes(name)) {
    alert("Sorry, that name already exists in the roster.")
  } else {
    roster.push(name)
  }
}

function remove(name) {
  var name = prompt("What name would you like to remove from the roster?")
  if (roster.includes(name)) {
    var index = roster.indexOf(name);
    if (index > -1) {
      roster.splice(index, 1)
    }
  } else {
    alert("Sorry, but " + name + " doesn't exist in our roster.")
  }
}

function display() {
  console.log(roster);
  alert("The roster has been displayed to the console.")
}

var quit = false
var use = prompt("Would you like to use this web app? (y/n)")

if (use === 'y' || use === 'Y') {
  while (!quit) {
    input = prompt("Would you like to add, remove, display, or quit?")
    if (input.toLowerCase() === 'add') {
      addNew()
    } else if (input.toLowerCase() === 'display') {
      display()
    } else if (input.toLowerCase() === 'remove') {
      remove()
    } else if (input.toLowerCase() === 'quit') {
      alert("Goodbye")
      quit = true
    } else {
      alert("I'm sorry, I didn't understand. Please press okay and then type add, remove, display, or quit in the textbox.")
    }
  }
} else if (use === 'n' || use === 'N') {
  alert('Goodbye')
  quit = true
} else {
  alert("I'm sorry, this app only recognizes 'y' or 'n' to answer the question. Refresh the page and try again.")
}
