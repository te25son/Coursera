#   ___  _     _           _
#  / _ \| |__ (_) ___  ___| |_
# | | | | '_ \| |/ _ \/ __| __|
# | |_| | |_) | |  __/ (__| |_
#  \___/|_.__// |\___|\___|\__|
#           |__/
#   ___       _            _           _
#  / _ \ _ __(_) ___ _ __ | |_ ___  __| |
# | | | | '__| |/ _ \ '_ \| __/ _ \/ _` |
# | |_| | |  | |  __/ | | | ||  __/ (_| |
#  \___/|_|  |_|\___|_| |_|\__\___|\__,_|
#
#  ____                                                _
# |  _ \ _ __ ___   __ _ _ __ __ _ _ __ ___  _ __ ___ (_)_ __   __ _
# | |_) | '__/ _ \ / _` | '__/ _` | '_ ` _ \| '_ ` _ \| | '_ \ / _` |
# |  __/| | | (_) | (_| | | | (_| | | | | | | | | | | | | | | | (_| |
# |_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_|_| |_| |_|_|_| |_|\__, |
#                  |___/                                       |___/

my_list = [1, 2, 3]  # this is a list object
my_list.append(4)  # this is a call to a function that lives inside the list object

# EVERYTHING IS AN OBJECT IN PYTHON

print(type([5, 6, 7]))              # class list
print(type(7))                      # class int
print(type("Hi!"))                  # class str
print(type({1: "A", 2: "B"}))       # class dict
print(type((1,2)))                  # class tuple
print(type(5.3435))                 # class float

# YOU CAN CREATE YOUR OWN CLASS

class Sample():
    pass

x = Sample()                        # class __main__.Sample
print(type(x))

class Dog():
    # create class object attributes
    species = 'canis lupus'

    # create method
    def __init__(self, breed, name):
        # create method attributes
        self.breed = breed
        self.name = name

spot = Dog(breed='lab', name='carlos')
print(type(spot))                   # class __main__.Dog
print(spot.breed)                   # lab
print(spot.name)                    # carlos
print(spot.species)                 # canis lupus

class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return Circle.pi * (self.radius ** 2)

    def set_radius(self, new_r):
        self.radius = new_r

my_circle = Circle()
print(my_circle.radius)             # 1 --prints the default value of 1 if radius is undefined by user

my_circle = Circle(3)
print(my_circle.radius)             # 3
print(my_circle.area())             # 28.26
my_circle.radius = 100
print(my_circle.area())             # 31400.0
my_circle.set_radius(40)
print(my_circle.radius)             # 40
