var person = {
  name: {
    first: 'Sammy',
    last: 'Rocket'
  },
  age: 25,
  occupation: 'Engineer',
  interests: ['Painting', 'Camping'],
  bio: function() {
    alert(this.name.first + this.name.last + ' is ' + this.age + ' years old and works as a(n) ' + this.occupation
    + '. ' + this.name.first + ' enjoys ' + this.interests[0] + ' and ' + this.interests[1])
  },
  greeting: function () {
    alert('What\'s up, I\'m ' + this.name.first + '!')
  }
}

// dot notation
person.name
person.age
person.occupation
person.interests
person.bio()
person.greeting()

// dot natation with subnamespace
person.name.first
person.name.last

// bracket notation
person['age']
person['occupation']
person['interests']
person['name']['first']
person['name']['last']

// this is very similar to how one would index an array
// probably why objects are sometimes call associative arrays
// objects map strings to values the same way arrays map numbers to values

// you can update values using the '=' sign and either dot or bracket notation
person.age = 32
person['occupation'] = 'Cotton Candy Maker'

// furthermore, you can set new values the same way
person['eyes'] = 'green'
person.height = '1.7m'
