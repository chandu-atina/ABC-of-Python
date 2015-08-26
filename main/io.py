import math

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

f = open('../files/workfile', 'w')
f.write("hi chandu")
f.close()
f = open('../files/workfile', 'r')

print(f.read())