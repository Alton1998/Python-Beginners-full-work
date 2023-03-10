# Sets {}
# Sets contain unordered, unique, immutable data types in a hash table.

# creating a set
s = {1, 2, 2, 2, 3, 4, 5}
print(s)

l = ['Bryan', 'Cairns', 46]
s = set(l)
print(s)

# Adding items
s.add('Hello')
s.update([1, 2, 3, 'Hello'])
print(s)

# Removing items
s.discard('Hello')  # Will not throw an error
s.remove(1)  # will throw an error
v = s.pop()  # Not useful
print(v)
print(s)

# Can not change items - remove and add
# s[0] = 'A' # Will not work
# print(s[0]) does not work since we are using hashtables

print(3 in s)
s.remove(3)
s.add(12)
print(s)

x = set('abcd')
y = set('cdefg')

s = x.union(y)  # All the elements that are in either set
print(f'Union {s}')
s = x.intersection(y)  # All the elements that are in both sets
print(f'Intersection {s}')

s = x.difference(y)  # All the elements that are in x but not y
print(f'Difference {s}')

s = x.symmetric_difference(y)  # All the elements that are in one of the sets
print(f'Symmetric Difference {s}')
