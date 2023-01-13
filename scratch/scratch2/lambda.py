# Lambda. The format for lambda is lambda arguments: expression
# Lambda creates a one-line function with some arguments and an expression. It will evaluate the expression and return the result.
add10 = lambda x: x + 10
'''So what we have done here is we've given an argument of x and an expression of x + 10. 
The expression adds 10 to the argument and returns a result.'''
print(add10(5))

# This would be the exact same result.
def add10_func(x):
    return x + 10
print(add10_func(5))

# But as you can see, the lambda function was much shorter.

# You can also have multiple arguments in lambda functions.
mult = lambda x,y: x*y
print(mult(2, 7))

# Lambda functions are typically used when you just need a simple one-line function that's used only once in your code.

# Let's look at some common methods that are used in tandem with lambda. First we'll create a list of tuples.
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
'''Now, we'll sort our list using the sorted method, then we'll make sure that we sort by the y index (from the lowest number to the highest number).
We do this using a lambda function, where key equals the lambda function that looks for the y value (index position 1) in each tuple in our list.'''
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D)
print(points2D_sorted)

# This would be the longer way of doing it.
points2D_b = [(1, 2), (15, 1), (5, -1), (10, 4)]

def sort_by_y(x):
    return x[1]

points2D_b_sorted = sorted(points2D_b, key=sort_by_y)
print(points2D_b)
print(points2D_b_sorted)

# As you can see, the lambda function was much quicker here.

'''Now, lets try lambda with the map function. The map function can transform each element in a list into something else by using a function.
It looks like this: map(func, seq). So, let's create a list then multiply everything in the list by 2 using map and lambda functions.'''
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(a)
print(list(b)) # You have to make this a list in order for it to print properly. Otherwise, it will just show that this is a map object.

# This would do the same thing. One could argue that this is even easier, but it's up for debate.
c = [x*2 for x in a]
print(c)

# Now, let's look at the filter function. It too gets a function and a sequence like the map function. It looks like this: filter(func, seq).
d = [1, 2, 3, 4, 5, 6]
# Now, let's say we only want to filter by the even numbers in the list and then print that out. We would do this.
e = filter(lambda x: x%2==0, d)
print(d)
print(list(e))

# Here is another way to accomplish this.
f = [x for x in d if x%2==0]
print(f)

# Finally, let's look at the reduce function. This function also takes a function and sequence argument like this: reduce(func, seq).
from functools import reduce
g = [1, 2, 3, 4]
product_g = reduce(lambda x,y: x*y, g)
print(g)
print(product_g)
# What we did here was 1*2=2, 2*3=6, 6*4=24.

# That's about it for lambdas right now. As you can see, it's a quick way to define a function and run it in one line.