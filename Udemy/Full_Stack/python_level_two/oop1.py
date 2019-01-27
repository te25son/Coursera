"""
Some more lesson examples for object oriented programming
"""

# INHERITANCE
class Animal():

    def __init__(self):
        print("Animal Created!")

    def whoami(self):
        print("Animal")

    def eat(self):
        print("Eating...")

class Dog(Animal):

    def __init__(self):
        # Animal.__init__(self)
        print("Dog Created!")

    def bark(self):
        print("Woof!")

    def fetch(self):
        print("Fetching...")

freddy = Animal()
freddy.whoami()
freddy.eat()

print("")

bruce = Dog()
bruce.whoami()
bruce.eat()
bruce.bark()
bruce.fetch()


# SPECIAL METHODS
class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title : {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("Book burning! Oh no :()")


b = Book("Killer Bees", "Amanda", 250)
print(b)
print(len(b))
del b
