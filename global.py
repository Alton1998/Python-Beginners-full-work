# Global

# Global keyword which allows code to modify a variable
# outside the current scope

x = 1


def test():
    # x = 6
    print(x)


test()
print(x)

# Global variable
counter = 0


def count():
    global counter
    counter += 1
    print(counter)


count()
