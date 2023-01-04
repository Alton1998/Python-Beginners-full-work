x = 5 * 3
print(x)

x = 1
print(x)

# Example of comments

# y = 2
# print(y)

# Booleans True or False (like a light switch)

x = True  # This is case-sensitive
y = False  # This is case-sensitive

# Comparisons - the building block of logic

print(f'x = {x}')
print(f'y = {y}')

print(f'Equal:{x == y}')
print(f'Not Equal:{x != y}')

print(f'Greater Than :{x > y}')
print(f'Greater than or equal:{x >= y}')

print(f'Greater than :{x > y}')
print(f'Greater than or equal :{x >= y}')

print(f'Less than :{x > y}')
print(f'Less than or equal :{x >= y}')

# Numbers - int float complex

# int
iVal = 34
print(f'iVal ={iVal}')

# float
fVal = 3.14
print(f'fVal ={fVal}')

import sys

print(sys.float_info)  # this gives the precision and other specs for float

# complex
#  number is made of 2 nos., a real and imaginary number

cVal = 3 + 6j
print(f'cVal = {cVal}')
# another way
cVal1 = complex(5, 3)
print(f'cVal1 = {cVal1}')
# extracting the real and imaginary part
print(f'real= {cVal1.real} imag={cVal1.imag}')

# Basic Numerical operations
x1 = 3
print(f'x={x1}')

y1 = x1 + 3
print(f'add = {y1}')

y1 = x1 - 1
print(f'subtract = {y1}')

y1 = x1 * 4.567
print(f'multiply = {y1}')

y1 = x1 / 0.5
print(f'divide = {y1}')

y1 = x1 ** 0.5
print(f'pow = {y1}')

y1 = x1 % 0.7
print(f'remaider = {y1}')
