'''There are two types of decorators: function decorators and class decorators. 
Function decorators are more common and an example is shown below.'''

'''@mydecorator
def myfunc():
    pass'''

# Function decorators extend the functionality of a function. 
def start_end_decorator(func):

    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

@start_end_decorator # This will do what is shown in line 21 below.
def print_name():
    print('Bob')

# print_name = start_end_decorator(print_name)

print_name()

'''Now what will happen if the function has some arguments in it? 
In that case, you must add *args and **kwargs as input parameters on your wrapper function.'''
import functools

def start_end_decorator_2(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator_2
def add5(x):
    return x + 5

result = add5(10)
print(result)

# Use the help method on the add5 function to verify that the used information from the function was preserved.
print(help(add5))
# Print the name of the function as well for verification purposes.
print(add5.__name__)

# Let's look at another example.
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')

greet('Billy')

# Nested decorators. You may stack decorators on top of each other.
def start_end_decorator_3(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

# Debug decorator.
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({signature})')
        result = func(*args, **kwargs)
        print(f'{func.__name__!r} returned {result!r}')
        return result
    return wrapper

# Stack decorators. They will be executed in the order they are listed.
@debug
@start_end_decorator_3
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

say_hello('Georgey')

# Class decorators. They do the same thing, but they are normally used when you want to maintain or update a state.
class CountCalls:

    def __init__(self, func):
        self.func = func
        # Keep track of how many times it is executed.
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)
        # print('Hello there')

#cc = CountCalls(None)
#cc()

@CountCalls
def say_hello_2():
    print('Hello')

say_hello_2()
say_hello_2()
say_hello_2()

'''With decorators you can calculate the execution time of a function (using a timer decorator), you can print out more information 
about a called function and its arguments (using a debug decorator), you can check if function arguments fulfill some requirements and
you can adapt the behavior accordingly (using a check decorator), you can register functions (plug-ins with decorators), you can cache return values,
add information or update the state of an object.'''