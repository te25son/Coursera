# ERRORS and EXCEPTIONS in PYTHON

try:
    f = open("hello.txt", "r")
    print(f.read())

except IOError:
    print("ERROR: COULD NOT FIND FILE")

else:
    print("SUCCESS")
    f.close()

try:
    f = open("hello.txt", "w")
    f.write("How are you today?")
    f.close()
    f = open("hello.txt", "r")
    print(f.read())

except IOError:
    print("ERROR!")

finally:
    print("This will work even if there's an error")
    f.close
