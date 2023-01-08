# Functions

def test():
    print("This is a function")


# Function with parameters

def sqft(w, h):
    v = w * h
    return v


# Call a function
test()
print(sqft(12, 3))

# Call a function multiple Times
for i in range(4):
    test()

# Functions and scope

# global scope

name = 'Alton'


# Functions can access the global scope

def global_scope_test():
    print(f'My name: {name}')


global_scope_test()

# Global scope cannot access the function scope

t = 10


def global_scope_test2():
    t = 50
    print(f'Functions Scope:{t}')


global_scope_test2()
print(f'Global Scope:{t}')


# positional and Keyword Arguments
def message(name, msg, age):
    print(f'Hello {name}, {msg}, you are {age} years old')


message("Alton", "Ola", 24)
message(msg="cool", name="Alton", age=24)  # Keywords


# Internal Functions
def counter():
    def display(count=0):
        print(f'Internal: {count}')

    for x in range(5):
        display(x)


counter()


# *args - positional variable length arguments

def multiple(*args):
    z = 1
    for num in args:
        print(f'Num ={num}')
        z *= num
    print(f'Multiply: {z}')


multiple(1, 23, 24343, 24323)


# **kwargs is used to pass a keyworded, variable length arguments
def person(**person):
    print(person)


person(name="Alton", age=34)

# Lambda Functions (anonymous functions)

sqft_lambda = lambda width=0, height=0: width * height

print(sqft_lambda(width=10, height=232))


# Packing and unpacking data

def pack(*nums):
    print(f'Packed: {nums}')
    for x in nums:
        print(f'Packed: {x}')


pack(1, 2, 3)


def unpack(a, b, c):
    print('Unpack')
    print(f'a={a}')
    print(f'b={b}')
    print(f'c={c}')


num = [1, 2, 3]
unpack(*num)

# Dictionary issue

d = dict(name='Alton', age=46, pet='Cat')
print('Packing Dictionary')
pack(*d)
print('Unpacking Dictionary')
unpack(*d)


# Packing and Unpacking a Dictionary
def packdict(**nums):
    print(f'nums = {nums}')
    for k in nums:
        print(f'Packed : {k} = {nums[k]}')


packdict(name="Alton", age=24, pet="dog")


# Unpacking a dictionary
def unpackdict(name, age, pet):
    print("Unpacking a dictionary")
    print(f"Name = {name}")
    print(f'Age = {age}')
    print(f'Pet = {pet}')


unpackdict(**d)


# Functions in an argument
def test2(name, age, pet):
    print(f'name = {name}')
    print(f'age = {age}')
    print(f'pet = {pet}')


def get_data():
    return dict(name='Alton', age=46, pet='Cat')


d = get_data()
test2(d['name'], d['age'], d['pet'])
test2(**d)
test2(**get_data())


# Function as an argument
def funky(kittens):
    d = kittens()
    print(d)


funky(get_data)
