# "name" here refers to an input parameter.
def print_name(name):
    print(name)
# The actual name that is inserted into the function here is called a function argument or just an argument.
print_name('Bob')

def foo(a, b, c):
    print(a, b, c)
# These are positional arguments.
foo(1, 2, 3)
# These are keyword arguments (order is not important here).
foo(c=1, b=2, a=3)
# You can also use a mixture of both, but you cannot use another positional argument after you've already used a keyword argument or you will get a SyntaxError.
foo(1, b=2, c=3)
# Sometimes keyword arguments are better because it's more readable.

'''You can also combine the argument types as input parameters within a function. The keyword argument here is called a default argument. 
Default arguments must come last in the input parameters or else you will get a SyntaxError.'''
def foo(a, b, c, d=4):
    print(a, b, c, d)

foo(1, 2, 3)
# Notice how 4 is printed here even though we specified only 1, 2, 3 in the argument.

# Pass any number of positional or keyword arguments into the function as input parameters.
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six=6, seven=7)
# This is great for variable length arguments.

# Forced keyword arguments.
def foo(a, b, *, c, d):
    print(a, b, c, d)
# Every argument after the star must be a keyword argument or else you will get a TypeError.
foo(1, 2, c=3, d=4)

# You can use the last keyword to make the last input parameter in a function a keyword argument.
def foo(*args, last):
    for arg in args:
        print(arg)
    print(last)
# The last argument here has to be a keyword argument or else you will get a TypeError.
foo(1, 2, 3, last=4)

# Unpacking arguments.
def foo(a, b, c):
    print(a, b, c)
# With a list.
my_list = [0, 1, 2]
foo(*my_list)
# Keep in mind that the number of items in the list here must match the number of input parameters in the function.

# With a dictionary. Must have the same keys as the input parameters in the function or else you will get a TypeError.
my_dict = {'a': 0, 'b': 1, 'c': 2}
foo(**my_dict)

# Local vs. global variables. Make a local variable global.
def foo():
    # This will make the number variable global rather than just local to the function.
    global number
    x = number
    number = 3 
    print = ('number inside function:', x)

number = 0
foo()
print(number)

# This local variable cannot be changed here because integers are immutable.
def foo(x):
    x = 5

var = 10
foo(var)
print(var)

# However, this local variable can be changed here because lists are mutable.
def foo(list_x):
    list_x.append(4)

my_list_x = [1, 2, 3]
foo(my_list_x)
print(my_list_x)

# Immutable objects within mutable objects CAN be changed. 
def foo(list_x):
    list_x.append(4)
    list_x[0] = -100

my_list_x = [1, 2, 3]
foo(my_list_x)
print(my_list_x)
# Be careful to not define a local variable (like list_x) before doing this or it will stay local and not be modified globally!

# You can also do this in order to get around it.
def foo(list_y):
    list_y += [200, 300, 400]
my_list_y = [1, 2, 3]
foo(my_list_y)
print(my_list_y)