# Lists []

# Create a list
x = ['Bryan', 'Cairns', 46]  # Can mix data types

print(f'List: {x}')  # Print the list
print(f'Len: {len(x)}')  # print the len

# Index and positioning - zero based

print(f'Zero:{x[0]}')  # First item is zero
print(f'Slice:{x[1:2]}')  # Slice the list

# Adding items - append, insert

x.append('Pizza')  # Adds at the end
x.append('Beer')  # Adds at the end
x.insert(1, 'Cats')  # Adds at a specific position
print(f'List: {x}')

# Removing items - remove, pop, delete
x.remove('Cats')  # Remove an item (removes first occurrence)
print(f'List:{x}')

i = x.index('Pizza')  # Will raise an error if not found
print(f'Food:{x.pop(i)}')
print(f'List:{x}')

i = x.index('Beer')  # Will raise an error if not found
del x[i]  # Delete a specific  item without it
print(f'List: {x}')

# Extending - adds elements from another list

y = ['Cats', 'Dogs', 'Birds']
x.extend(y)
print(f'List: {x}')

# Sort - sort,reverse
x.remove(46)  # Errors without removing
x.sort()
print(f'Sort :{x}')
print(f'Sort: {x}')
x.reverse()
print(f'reverse: {x}')

# Copy

y = x.copy()  # Copies elements into a new list
y.reverse()
y.append("Apples")
print(f'Original: {x}')
print(f'New: {y}')

# Delete the whole thing

del y

# Clear
x.clear()
print(f'Cleared: {x}')
print(f'Len: {len(x)}')

# Lists can contain other lists
x = []
y = [1, 2, 3]
z = ['Bryan', 'Cairns']
x.append(y)
x.insert(0, z)

print(f'Lists in lists:{x}')
print(f'Len: {len(x)}')
print(f'0:{x[0][0]}')
print(f'1:{x[1][2]}')

# Changin items - positional
x = [1, 2, 3, 4, 5]
x[2] = 'TEST'
print(x)
