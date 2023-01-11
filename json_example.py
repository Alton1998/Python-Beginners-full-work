import json

filename = 'json.txt'

outD = dict(name='Alton',age=24,pet='Dog')
s = json.dumps(outD)
print(f'String={s}')

inD = json.loads(s) # Load the dictionary from the string
print(f'Dictionary={inD}')

# To File

with open(filename,'w') as f:
    json.dump(outD,f)

# From File

with open(filename,'r') as f:
    p = json.load(f)

print(f'Type:{type(p)}')

