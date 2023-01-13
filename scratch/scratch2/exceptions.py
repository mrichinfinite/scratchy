# Errors and Exceptions 

'''Errors and exceptions will be commented out in order to not raise exceptions during run time.
Remove the comments to try the code at runtime.'''

'''You can raise an exception in Python when a certain condition is met.
x = -5 
if x < 0:
    raise Exception('x should be a positive number')'''

'''You can also use an assert statement to throw an error is your assertion is not true.
x = -5
assert(x >= 0), 'x is not a positive number'
'''

'''You can also do a try/except block. This will try a block of code and raise an exception if the 
code fails at run time.'''
try:
    a = 5 / 0
except:
    print('An error occurred. You cannot divide by zero.')

# You can do the same thing using the built-in error handling.
try:
    a = 5 / 0
except Exception as e:
    print(e)

# If you know what the error type is you can just put it directly into the code.
try:
    a = 5 / 0
except ZeroDivisionError:
    print('You cannot divide by zero.')

try:
    a = 6
    b = a + '10'
except TypeError as f:
    print(f)

# You may also add an else clause to your try/except block in case no error occurred.
try:
    a = 6
    b = a + 10
except TypeError as f:
    print(f)
else:
    print('Looking good!')

# You may also add a finally clause, which runs whether there was an exception or not.
try:
    a = 6
    b = a + 10
except TypeError as f:
    print(f)
else:
    print('Looking good!')
finally:
    print('Cleaning up...')

try:
    a = 6
    b = a + '10'
except TypeError as f:
    print(f)
else:
    print('Looking good!')
finally:
    print('Cleaning up...')

# You may also define your own exception by defining an Error class via subclassing from the base Exception class.
class ValueTooHighError(Exception):
    pass

def test_value(x):
    if x > 100:
        raise ValueTooHighError('The value is too high.')
# Remove the hash below to test this function.
# test_value(200)

# You may also add this function to a try/except block.
try:
    test_value(200)
except ValueTooHighError as y:
    print(y)

'''You'll want to keep your Error classes small but useful. Let's try one more, but we'll make it opreate a bit differently this time. 
Again, the base class will be the Exception class.'''
class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value_2(x):
    if x < 5:
        raise ValueTooSmallError('The value is too small:', x)

try:
    test_value_2(1)
except ValueTooSmallError as y:
    print(y.message, y.value)
# As you can see, tje message was printed along with the value.
