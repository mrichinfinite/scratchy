# Generators: syntax starts off similar to a regular function but you use a yield statement instead of a return statement.

# Define the generator.
def mygenerator():
    yield 1
    yield 2
    yield 3
# Call the generator using a variable, printing the variable will just show that it's a genrator object.
g = mygenerator()
print(g)

# Iterate through the generator.
# for i in g:
    # print(i)

# Iterate through the generator but pause at first yield statement.
value = next(g)
print(value)
# Same as above, but this will of course pause at the next yield statement.
value = next(g)
print(value)

# Same as above, but this will of course pause at the next yield statement.
value = next(g)
print(value)

# Generators will return a StopIteration if there is no further yield statement.
# value = next(g)
# print(value)

# The above will print this if uncommented:
# Traceback (most recent call last):
  # File "C:\Users\matrich\Documents\scratch\scratch2\generators.py", line 28, in <module>
    # value = next(g)
# StopIteration

# Can use generators as input to other functions & methods that also contain iterables. Calculate 1 + 2 + 3 in mygenerator2().
def mygenerator2():
    yield 1
    yield 2
    yield 3

g = mygenerator2()
# Using sum method here.
print(sum(g)) 

# Return new list with all the objects in a sorted order.
def mygenerator3():
    yield 3
    yield 2
    yield 1

g = mygenerator3()
# Sort the objects in order.
print(sorted(g))

# Execution of a generator function.
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1
# Countdown starting from 4.
cd = countdown(4)
# Iterate through generator beginning with the generator's print statement and stopping at first yield statement.
value = next(cd)
# Print first yield statement result.
print(value)
# Print next yield statement.
print(next(cd))

# print(next(cd))
# print(next(cd))
# print(next(cd))
# After this point, StopIteration will be outputted.

# The advantages of generators. 1st of all: very memory efficient.
import sys # You will see why this is needed below.
# Start with a regular function.
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

# Print all the values in the list from 0-9.
print(firstn(10))
# Calculate the same of all items in the list.
print(sum(firstn(10)))
# Print size of object in bytes.
print(sys.getsizeof(firstn(10)))
# The above example is very memory intensive. What if we use a generator instead?
def firstn_generator(n):
    num = 0 # No need to call the empty list, just start by declaring num.
    while num < n:
        yield num
        num += 1
# Calculate the same of all items in the list.
print(sum(firstn_generator(10)))
# Print size of object in bytes.
print(sys.getsizeof(firstn_generator(10)))
# As you can see, the generator object is smaller, this helps with large data sets. Let's paint the picture again.
print(sys.getsizeof(firstn(1000000)))
# vs.
print(sys.getsizeof(firstn_generator(1000000)))
# HUGE difference!

# 2nd advantage of generator object: we do not have to wait until all the elements have been generated before we start to use them.

# Fibonacci sequence.
def fibonacci(limit):
    # 0 1 1 2 3 5 8 13 ...
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
# Define variable which loops through the sequence, set limit to 30 as an example.
fib = fibonacci(30)
for i in fib:
    print(i)

# Generator expressions. Just like list comprehensions but with parentheses instead of square brackets. 

# As an initial example, here is a list comprehension defined in a variable. All even elements from 0-9 will be printed.
mylist = [i for i in range(10) if i % 2 == 0]
print(mylist)
# Now, same thing but using a generator object defined in a variable.
mygenerator4 = (i for i in range(10) if i % 2 == 0)
# If I want to print a list just like before, but this time using the generator object, I can do so using the list method.
print(list(mygenerator4))
# Can for loop through it too.
mygenerator5 = (i for i in range(10) if i % 2 == 0)
for i in mygenerator5:
    print(i)

# Let's check out a memory comparison again.
mylist2 = [i for i in range(1000000) if i % 2 == 0]
print(sys.getsizeof(mylist2))
mygenerator6 = (i for i in range(1000000) if i % 2 == 0)
print(sys.getsizeof(mygenerator6))
# MASSIVE difference!