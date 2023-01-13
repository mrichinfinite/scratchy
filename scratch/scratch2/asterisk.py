'''The Asterisk (*) Operator (or Star Operator):
Used for multiplication and power operations, the creation of lists or tuples with repeated elements, 
for *args and **kwargs and keyword-only parameters, for unpacking lists, tuples or dictionaries into
function arguments, for unpacking lists, tuples, dictionaries or sets into a new list, for merging 
lists, tuples, dictionaries or sets into a new list and for merging two dictionaries.'''

# Multiplication operation.
result = 5 * 7
print(result)

# Power operation.
result2 = 2**4
print(result2)

# List with repeated elements (a list of 10 zeros).
zeros = [0] * 10
print(zeros)

# Let's try a different one.
zeros2 = [0, 1] * 10
print(zeros2)

# Tuple with repeated elements.
zeros3 = (0, 1) * 10
print(zeros3)

# Repeated string.
astring = "ABC" * 10
print(astring)

# Using the asterisk or star for *args, **kwargs.
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six=6, seven=7)

# Using it for keyword-only arguments/parameters.
def foo2(a, b, *, c):
    print(a, b, c)
    
foo2(1, 2, c=3)

# Using it for unpacking lists.
def foo3(a, b, c):
    print(a, b, c)
# The number of elements below must match the number of parameters defined in the function above.    
my_list = [0, 1, 2]
foo3(*my_list)

# Using the asterisk or star for unpacking dictionaries.
def foo4(a, b, c):
    print(a, b, c)
'''The number of elements below must match the number of parameters defined in the function above.
Also, the name of each key in the dictionary must match the name of the parameters defined in the 
function above.'''
my_dict =  {'a': 1, 'b': 2, 'c': 3}
foo4(**my_dict)

'''Unpacking data types.
You can unpack the elements of a list, tuple or set into single and multiple remaining elements.'''
numbers = [1, 2, 3, 4, 5, 6]
# Unpack all elements (except for the last one) into a list. Then, print only the last element.
*beginning, last = numbers
print(beginning)
print(last)

# You can do this with a tuple as well, but it will still print as a list in the output.
numbers2 = (1, 2, 3, 4, 5, 6)

*beginning, last = numbers
print(beginning)
print(last)

# Put the asterisk or star in front of "last" instead of "beginning" and see what happens.
numbers2 = (1, 2, 3, 4, 5, 6)

beginning, *last = numbers
print(beginning)
print(last)

# Put it in the middle and see what happens.
numbers2 = (1, 2, 3, 4, 5, 6)

beginning, *middle, last = numbers
print(beginning)
print(middle)
print(last)

# You can even do this!
numbers2 = (1, 2, 3, 4, 5, 6)

beginning, *middle, secondlast, last = numbers
print(beginning)
print(middle)
print(secondlast)
print(last)

# Merge data types to create a new merged list.
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]

new_list = [*my_tuple, *my_list]
print(new_list)

# You can do the same thing with a set.
my_tuple = (1, 2, 3)
my_set = [4, 5, 6]

new_list = [*my_tuple, *my_set]
print(new_list)

# You can also merge two dictionaries into one.
dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}

my_dict = {**dict_a, **dict_b}
print(my_dict)