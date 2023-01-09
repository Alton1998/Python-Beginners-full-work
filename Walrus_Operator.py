# Walrus operator and global
# Added in python 3.8 looks like :=

# Assign a variable from an expression
# Must have the right version
(y := len('hello'))
print(y)
people = ['Alton', "Lavin", "Dsouza"]

if (n := len(people)) <= 3:
    print(n)

lines = []


def canAdd(max=5):
    global lines  # Allows us to ensure we are using the global variable
    if allowed := (count := len(lines)) < max:
        print(f'You can enter {max - count} more')
    return allowed


while canAdd():
    lines.append(l := input('Enter a line:'))

print(f'You entered:{lines}')
