# Dictionary {k:v, k:v}
# indexed by keys, which can be any immutable keys

# Create a dictionary
d = {'pet': 'dog', 'age': 5, 'name': 'spot'}
print(d)
d = dict(pet='dog', age=5, name='spot')
print(d)

# Get keys and values
print(f'Items:{d.items()}')
print(f'Keys  {d.keys()}')
print(f'Values:{d.values()}')

# Getting a value from the key
print(f'Name : {d["pet"]}')
