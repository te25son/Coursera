var person = {
  name: ['Bob', 'Smith'],
  age : 32,
  gender: 'male',
  interests: ['music', 'camping'],
  bio: function() {
    alert(
      this.name[0]
      + ' '
      + this.name[1]
      + ' is '
      + this.age
      + ' years old. '
      + this.name[0]
      + ' likes '
      + this.interests[0]
      + ' and '
      + this.interests[1]
      + '.'
    )
  },
  greeting: function() {
    alert(
      'Hi, I\'m '
      + this.name[0]
      + '!'
    )
  }
}


var car = {
  make: 'Dodge',
  model: 'Avenger',
  year: 1997,
}

car.make // Dodge
car.model // Avenger
car.year // 1997

var person2 = {
  name: {
    first: 'Bob',
    last: 'Smith',
  }
}

person2.name.first // Bob
person2.name.last // Smith

// you can also use bracket notation
person['name'] // ['Bob', 'Smith']

var myObject = {
  a: "hello",
  b: [1, 2, 3],
  c: {
    nested: ['a', 'b']
  }
}

myObject['a'] // hello
myObject.a // hello

myObject['b'][1] // 2
myObject.b[1] // 2

myObject['c']['nested'][1] // b
myObject.c.nested[1] // b

// change the value of an existing value inside an object
// call the item and set the value to it's new value
car.year = 2000
// OR
car['year'] = 2000

// to see whole object
console.dir(car)

// iterate over an object
// you can use a 'for in' statement
// get the keys of an object
for (var key in car) {
  console.log(key);
}

// get the values of keys in an object
for (var key in car) {
  console.log(car[key])
}
