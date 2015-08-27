import math
import json

s = 'Hello, world.'
print(str(s))
print(repr(s))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))
print()
print('~~~~~~~~~~~')
print()
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))
print()
print('~~~~~~~~~~~')
print()
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

s='202'
print(s.rjust(7))
print(s.ljust(7))
print(s.center(7))
print(s.zfill(7))

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

print('This {food} is {adjective}.'.format(
            food='spam', adjective='absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                       other='Georg'))

"""
    '!a' (apply ascii()), 
    '!s' (apply str()) and
    '!r' (apply repr()) can be used to convert the value before it is formatted
"""
print('The value of PI is approximately {!r}.'.format(math.pi))
print('The value of PI is approximately {0:.3f}.'.format(math.pi))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))
    
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

"""
    File Operations
"""

f = open('../files/workfile1', 'w')
value = ('the answer', 42)
s = str(value)
f.write("hi chandu")
f.write(s)
f.close()

f = open('../files/workfile1', 'r')
print(f.read())
f.close()

f = open('../files/workfile', 'r')
for line in f:
    print(line, end='')
    
""" list(f) or f.readlines() """

print('\n',f.tell())

print(f.seek(5))
"""
In text files (those opened without a b in the mode string), 
only seeks relative to the beginning of the file are allowed 
(the exception being seeking to the very file end with seek(0, 2)).

f.seek(-3, 2) # Go to the 3rd byte before the end (in binary mode)

"""

print(f.seek(0,2))

""" Closing file in better way. Using with keyword will automatically 
take care of closing file even during exceptions. """

with open('../files/workfile1', 'r') as f:
    print(f.read())

""" Saving structured data with json """
with open('../files/workfile1', 'r') as f:
    print(json.dumps(f.read()))

f = open('../files/workfile1', 'w')

json.dump(x, f) # save json ormat to file f

f = open('../files/workfile1', 'r')

x = json.load(f) #decode object from json file
