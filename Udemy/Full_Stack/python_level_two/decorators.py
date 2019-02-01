#  ____                           _
# |  _ \  ___  ___ ___  _ __ __ _| |_ ___  _ __ ___
# | | | |/ _ \/ __/ _ \| '__/ _` | __/ _ \| '__/ __|
# | |_| |  __/ (_| (_) | | | (_| | || (_) | |  \__ \
# |____/ \___|\___\___/|_|  \__,_|\__\___/|_|  |___/

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


reassigned = funA
print(reassigned())
