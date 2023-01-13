# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter 
'''Counter stores elements in a string as dictionary keys and counts how many times 
that element exists in the string, then stores that number as a value in the dictionary.
Each value will correspond to the correct key in the dictionary based off of how many
times it is seen in the string.'''
a = "My String"
my_counter = Counter(a)
print(my_counter)
# One more example to illustrate the point. Again, the string character is the key, the count is the value.
b = "xxxxxyyyyyzzzzz"
my_counter2 = Counter(b)
print(my_counter2)
# All dictionary methods will work on this dictionary as well. See the dictionaries lesson for methods.

# Here's a method to try. What is the 1st and 2nd most common key-value pair in the Counter dictionary we specify?
c = "aaabbbbccccc"
my_counter3 = Counter(c)
print(my_counter3.most_common(1))
print(my_counter3.most_common(2))
# Now what if I want to ONLY see the most common key?
print(my_counter3.most_common(1)[0][0])
# What if I want to change this Counter dictionary into a list?
print(list(my_counter3.elements()))
# Now what if I want to remove the duplicates from the list?
my_counter4 = list(my_counter3)
print(my_counter4)
# Now what if I want to convert the list back to a dictionary?
my_counter5 = Counter(my_counter4)
print(my_counter5)
# Can I start by creating a Counter dictionary for a list itself rather than a string? Yes!
d = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8]
my_counter6 = Counter(d)
print(my_counter6)
# As you can see, you can use Counter on any iterable data type (strings, lists, tuples, etc.)

# Now, let's take a look at namedtuple.
from collections import namedtuple
# This will create a class called Point with the fields x and y.
Point = namedtuple('Point', 'x,y')
# Now we will create our points within a variable.
pt = Point(1, -4)
# Now we will print the points in two different ways to show some examples.
print(pt)
print(pt.x, pt.y)

# Time to look at OrderedDict.
from collections import OrderedDict
# This is just like a regular dictionary but it remembers the order in which the items are inserted into the dictionary.
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['aa'] = 5
ordered_dict['bb'] = 6
print(ordered_dict)
'''Keep in mind that OrderedDict is not really needed with Python 3.7 and above since the dict class has the ability to
do this by default, but it's nice to know about OrderedDict if you're working with older Python versions.'''

# Here's how you can achieve the same result with Python 3.7 and above.
ordered_dict2 = {}
ordered_dict2['a'] = 1
ordered_dict2['b'] = 2
ordered_dict2['c'] = 3
ordered_dict2['d'] = 4
ordered_dict2['aa'] = 5
ordered_dict2['bb'] = 6
print(ordered_dict2)

# Now, let's take a look at defaultdict.
from collections import defaultdict
'''With defaultdict, a default value will be given to a key that has not been set yet. So, let's start by defining a dictionary and
putting the integer class inside of defaultdict. What this will do is give us an integer whenever we call a key
that has not been defined yet.'''
d = defaultdict(int)
# Now, let's create another dictionary.
d['a'] = 1
d['b'] = 2
'''Now, let's call the 'c' key, which does not exist yet. We will see that a default value (an integer) is automatically assigned to 
the new key'''
print(d['c'])
# Let's try the same thing but with a float.
e = defaultdict(float)
e['a'] = 1
e['b'] = 2
e['c'] = 3
print(e['d'])
# Let's try it with a list now.
f = defaultdict(list)
f['a'] = 1
f['b'] = 2
f['c'] = 3
f['d'] = 4
print(f['e'])
'''As you can see, defaultdict allows you to pass in many different data types as input parameters. With regular dictionaries,
if you call a key that does not exist, you will get a KeyError. However, with defaultdict you can get around this.'''

# Finally, let's look at deque.
from collections import deque
# Create a deque.
d = deque()
# Add items to the deque (or to the end of the deque if items already exist within the deque).
d.append(1)
d.append(2)
print(d)
# Add an item to the beginning of the deque.
d.appendleft(3)
print(d)
# Remove an item from the end of the deque.
d.pop()
print(d)
# Remove an item from the beginning of the deque.
d.popleft()
print(d)
# Remove all items from the deque.
d.clear()
print(d)
# Add a list of items to the end of the deque.
d.extend([4, 5, 6])
print(d)
# Add a list of items to the beginning of the deque.
d.extendleft([7, 8, 9])
print(d)
# Rotate all elements one space to the right.
d.rotate(1)
print(d)
# Rotate all elements two spaces to the right.
d.rotate(2)
print(d)
# Rotate all elements one space to the left.
d.rotate(-1)
print(d)
# Rotate all elements two spaces to the left.
d.rotate(-2)
print(d)