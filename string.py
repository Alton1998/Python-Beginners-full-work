# string
# list of characters

for x in 'hello':
    print(f'{x}={ord(x)}')

## How To make a string

first = "Bryan"  # Can be double quote
last = 'Cairns'  # Can be single quote
print(first + ' ' + last)
print(f'Hello my name is {first} {last}')

hers = "Heather's"
print(hers)

# Under the hood - unicode(UTF8)

s1 = chr(72)
s2 = chr(105)
print(s1 + s2)

print(chr(8710))  # Way beyound Ascii

# Escape Characters - start with a slash \

print(f'Hello{chr(13) + chr(10)}World')
print(f'Hello\r\nWorld')
strTest = "Hello\tWorld"
print(strTest)

hers = 'Heather\'s'
print(hers)

# Must Format Strings to avoid errors

name = "Bryan"
age = 46

# print(name + ' '+ age) Error
print(f'My name is {name} I am {age} years old')
print("My name is %s, I am %i years old!" % (name, age))

mystr = "Hello World, this is a string"

print(len(mystr))  # Get the length
print(mystr * 3)  # Repeat
print(mystr.replace('Hello', "Hola"))
print(mystr.split(','))  # Split
print(mystr.startswith("H"))
print(mystr.endswith("!"))
print(mystr.upper())
print(mystr.lower())
print(mystr.capitalize())

# Slicing or getting a sub string
print(mystr[0:5])
print(mystr[6:])
print(mystr[-7:])
print(mystr[6:11])

# indexes - the position of
l = ','
c = mystr.find(l)  # -1 if not found
print(f'Find Returned {c}')

i = mystr.index(l)
print(f'Find Returned {i}')

x = mystr[:i]
print(x)
