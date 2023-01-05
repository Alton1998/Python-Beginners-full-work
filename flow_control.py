# IF Else ELif

# if Condiion
x = True
if x:
    print('yes')
else:
    print('no')

# Condition Evaluations (True - run | False - not run)

x = 100
y = 25
if y == x:
    print('equal to')
if y != x:
    print('not equal to')
if y < x:
    print('less than')
if y > x:
    print('greater than')
if y <= x:
    print('less than or equal to')
if y >= x:
    print('greater than or equal to')

# elif is the switch solution
x = 10
if x == 25:
    print('x = 25')
elif x == 50:
    print('x = 50')
elif x == 75:
    print('x =75')
else:
    print('catch all here')

# Nested Statements

x = 82
if x > 50:
    print('over 50')
    if x > 60:
        print('over 60')
        if x > 70:
            print('over 70')

# while loop

x = 0
while x < 10:
    x += 1
    print(f'x = {x}')
print('Test 1 is done')

x = 0
# while x < 10:
#     pass
# print('Test 2 is done')

# Continue and break

x = 0
while True:  # Loop Forever
    x += 1
    if x < 5:
        print(f'x<5:{x}')
    print(f'Do something {x}')

    if x == 10:
        print(f'Exiting x={x}')
        break

print('Complete!')

# For loop and range

# For loop on lists, tuples, sets

x = [1, 2, 3, 4]  # List

t = (1, 2, 3, 4)  # Tuple

s = {1, 2, 3, 4}  # Set

print("List:")
for i in x:
    print(f'i={x}')

print("Tuple")
for i in t:
    print(f'i={i}')

print("Set")
for i in x:
    print(f'i = {i}')

# For loop on Dictionaries
x = dict(Bryan=46, Tammy=48, Heather=28, Chris=30)
print(x)

for k in x.keys():
    print(f'Keys:{k}')

for k, v in x.items():
    print('f Key:{k}')
    print('f Value:{v}')

# Range
x = range(5)
for i in x:
    print(f'Range:{i}')

# Range start stop and step

x = range(5, 20, 3)
for i in x:
    print(f'Range1:{i}')
