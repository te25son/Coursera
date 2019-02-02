# WARMUP...

def hello(name="human"):
    return "Hello {}".format(name)

print(hello())

# assign function to another variable name
say_hi = hello

print(say_hi())

def funA(name="human"):
    print("funA()")

    def funB():
        return "funB()"

    def funC():
        return "funC()"

    # return a function inside a function
    if name == 'human':
        return funB
    else:
        return funC


reassigned = funA()
print(reassigned())

x = funA()
y = x()
if y == 'funB()':
    print("TRUE")
else:
    print("FALSE")

# FUNCTION AS ARGUMENT
def hello_there():
    return "Hello there"

def gen_ken(func):
    print(func() + "... General Kenobi")

gen_ken(hello_there)

# NOW ON TO DECORATORS FOR REAL
#  ____                           _
# |  _ \  ___  ___ ___  _ __ __ _| |_ ___  _ __ ___
# | | | |/ _ \/ __/ _ \| '__/ _` | __/ _ \| '__/ __|
# | |_| |  __/ (_| (_) | | | (_| | || (_) | |  \__ \
# |____/ \___|\___\___/|_|  \__,_|\__\___/|_|  |___/

def new_deco(func):

    def wrap_func():
        print("code here before executing func")
        func()
        print("func() has been called")

    return wrap_func

@new_deco  # this does the same as the commented code below
def func_needs_deco():
    print("i need a decorator")

# func_needs_deco = new_deco(func_needs_deco)
# func_needs_deco()

func_needs_deco()
