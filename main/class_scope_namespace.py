import this
def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ClassName:
    """
    <statement-1>
    .
    .
    .
    <statement-N>
    """

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'

print(MyClass.f(this))

print(MyClass.i)

print(MyClass.f)

print(MyClass.__doc__)

x = MyClass()

print(x.f())

print(x.i)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class MyClassWithInitOverRide:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'
    
    """ class instantiation automatically invokes __init__() """
    def __init__(self):
        print("Init called on object initialization")
        self.data = []
        
y = MyClassWithInitOverRide()

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        
x = Complex(3.0, -4.5)
print("Real : ",x.r," Imaginary : ",x.i)
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

"""
MyClass.f(this)
x.f()
Both are same because -
The special thing about methods is that the object is passed as the first argument of the function
"""

# Class and Instance Variable

class Dog:
    kind = 'canine'         # class variable shared by all instances
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
        

# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1
    def g(self):
        return 'hello world'
    h = g

# Methods may call other methods by using method attributes of the self argument:
class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)
        
# Inheritance

"""
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
    
    
class DerivedClassName(modname.BaseClassName): (when base class defined in another module)

"""

#override
#methodlookback

""" 
Python has two built-in functions that work with inheritance:
    Use isinstance() to check an instance’s type: isinstance(obj, int) 
    Use issubclass() to check class inheritance: issubclass(bool, int) 
"""

# Multiple Inheritance
"""
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>

multiple inheritance exhibit one or more diamond relationships, to avoid that 
dynamic algorithm linearizes the search order in a way that preserves the 
left-to-right ordering specified in each class, that calls each parent only once

In the above example Base1 > Base2 > Base3
"""

# Odds and Ends
""" model class """
class Employee:
    pass

john = Employee() # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000


#Exceptions Are Classes Too
#raise Class
#raise Instance

""" define except from more specific to more generic """
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

#Iterators

"""
for loop calls iter() function for iterator. It inturn calls __next__() function repeatedly
When list ends __next__() will raise StopIteration exception which terminates the for loop

"""

for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("../files/workfile1"):
    print(line, end='')

"""
You can call the __next__() method using the next() built-in function; 
this example shows how it all works:
"""
s = 'abc'
it = iter(s)
print(next(it))
print(next(it))
print(next(it))

"""
To add iterator behavior to your classes, define an __iter__() method 
which returns an object with a __next__() method. 
If the class defines __next__(), then __iter__() can just return self:
"""

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    
rev = Reverse('spam')
iter(rev)
for char in rev:
    print(char)
    
# Generators
"""
 Generators are a simple and powerful tool for creating iterators.
"""
def reverse(data):
    for index in range(len(data)-1, -1, -1): #range(start,stop[,step])
        yield data[index]

for char in reverse('golf'):
    print(char)
        
#reverse("chandu")

# Generator Expressions
print(sum(i*i for i in range(10)))

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec)))

from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
print(sine_table)

#unique_words = set(word  for line in page  for word in line.split())

#valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
x= list(data[i] for i in range(len(data)-1, -1, -1))
print(x)

