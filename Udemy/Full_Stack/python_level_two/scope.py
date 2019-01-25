# scope

x = 25  # global x

def my_fun():
    x = 50
    return x

print(x)  # 25
print(my_fun())  # 50
my_fun()
print(x)  # 25

y = 35

def other_fun():
    global y
    y = 60
    return y

print(y)  # 35
print(other_fun())  # 60
other_fun()
print(y)  # 35


name = "Global"

def greet():
    name = "John"
    def hello():
        print("Hello {}".format(name))

greet()  # NOTHING IS RETURNED
