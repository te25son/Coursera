import one

print("top level two.py")

one.fun()

if __name__ == "__main__":
    print("two.py being run directly")
else:
    print("two.py has been imported")
