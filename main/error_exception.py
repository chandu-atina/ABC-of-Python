#while True :print('Hello world')

#
"""
    try :
        --------
    except ValueError:
        --------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
    try :
        --------
    except (RuntimeError, TypeError, NameError):
        --------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    try :
        --------
    except except OSError as err:
        --------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
    try :
        --------
    except ValueError:
        pass
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    try :
        --------
    except :
        print("--------")
        raise
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
    
    The use of the else clause is better than adding additional code to the try clause 
    because it avoids accidentally catching an exception that wasn’t raised by the code 
    being protected by the try ... except statement.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
"""
#
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except  ValueError:
        print("Oops!  That was no valid number.  Try again...")
        pass
    
import sys

try:
    f = open('../files/workfile1')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
##########################################################
# exception instance with the arguments stored in instance.args
###########################################################

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)
    
# raise Error
"""raise NameError('HiThere') """

# User Defined Exception
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    
try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)
    
# raise MyError('oops!')

"""
Best practice : one base exception and extend it for specific exception in project
# Most exceptions are defined with names that end in “Error,” 
# similar to the naming of the standard exceptions
"""
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
        
# Clean-up Actions (finally)
"""
finally is called when
    exception raised
    no exception
    exception caught
    exception not caught (re-raised after finally block executed)
    break in try/else
    continue in try/else
    return in try/else
"""

try:
    #raise KeyboardInterrupt
    print("commented raise exception for rest of the program to run")
finally:
    print('Goodbye, world!')
########################################################

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
        
divide(2, 1)

divide(2, 0)

divide("2", "1")

# Predefined Clean-up Actions
"""
# File is not closed in below code

for line in open("myfile.txt"):
    print(line, end="")

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# File is automatically closed when opened with "with" clause

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
        
"""