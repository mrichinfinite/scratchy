# Tuple: ordered, immutable, allows duplicate elements

# You can define a tuple with or without parentheses.
mytuple = ("Max", 28, "Boston")
print(mytuple)
# OR
mytuple = "Max", 28, "Boston"
print(mytuple)

# If you want only a single element inside of your tuple, it would look like this (kind of odd, but it works):
mytuple2 = ("Max",)
print(type(mytuple2))

# Create a tuple from an iterable (like a list) using the tuple() function.
mytuple3 = tuple(["Bill", 29, True])
print(mytuple3)

# Access elements in tuple.
item = mytuple[0]
print(item)
item2 = mytuple[1]
print(item2)
# Can access elements from end of list too (just like in lists).
item3 = mytuple[-1]
print(item3)

# Also, keep in mind that you cannot change elements in a tuple like you can with lists because a tuple is immutable.

# Iterate over a tuple (again, you don't have to call this "i", it could be "x" or whatever you want).
for i in mytuple:
    print(i)

# Check if an element is inside of a tuple using an if statement.
if "Max" in mytuple:
    print("yes")
else:
    print("no")
if "Tim" in mytuple:
    print("yes")
else:
    print("no")

# Get the number of elements inside of a tuple.
my_tuple = ('a', 'p', 'p', 'l', 'e')
print(len(my_tuple))

# Count number of elements inside of a tuple.
print(my_tuple.count('p'))
print(my_tuple.index('a'))
print(my_tuple.index('e'))

''' Get the first index of an element inside of a tuple 
(If you specify an element that is not inside of the tuple then you will get a ValueError, so be careful). '''
print(my_tuple.index('p'))
print(my_tuple.index('a'))
print(my_tuple.index('l'))

# Convert a tuple into a list and vice versa.
my_list = list(my_tuple)
print(my_list)

my_tuple2 = tuple(my_list)
print(my_tuple2)

# Slicing tuples.
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Define a range and print it.
b = a[2:5]
print(b)
# Start from the beginning of the tuple and end at the specified index position.
c = a[:5]
print(c)
# Start from the specified index position and end at the end of the tuple.
d = a[2:]
print(d)
# Step through the tuple, define how many steps to take.
e = a[::2]
print(e)
# Reverse it.
f = a[::-2]
print(f)

# Unpacking a tuple.
my_tuple_1 = "Max", 28, "Boston"

name, age, city = my_tuple_1
print(name)
print(age)
print(city)

''' Unpack multiple elements from a tuple using a star. We will print the first element in the tuple, 
then the last element in the tuple and finally we will print everything in between (as a list). '''
my_tuple_2 = (0, 1, 2, 3, 4)

i1, *i2, i3 = my_tuple_2
print(i1)
print(i3)
print(i2)

''' Compare a tuple and a list based off of number of bytes and also based off of time 
(by creating a million lists and a million tuples). The purpose of this is to show that tuples are sometimes more efficient than lists 
(especially when working with large data). '''
import sys
my_list_1 = [0, 1, 2, "hello", True]
my_tuple_3 = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list_1), "bytes")
print(sys.getsizeof(my_tuple_3), "bytes")

import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
