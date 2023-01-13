import random

# This will print a random float in the range of 0 to 1.
a = random.random()
print(a)

# Now, if you want to have a specific range, you can do this.
b = random.uniform(1, 10)
# This will print a random float between 1 and 10.
print(b)

# You may do the same thing, but with an integer.
c = random.randint(1, 10)
print(c)

# You can do the same thing as above, but without ever including the final number in the printed output.
d = random.randrange(1, 10)
print(d)

'''You can use this method for normal distribution of a random number 
with a mean of 0 and standard deviation of 1 (this could be useful in statistics).'''
e = random.normalvariate(0, 1)
print(e)

# The choice() method will pick a random element from a previously defined list.
mylist = list("ABCDEFGH")
print(mylist)
f = random.choice(mylist)
print(f)

'''Use the sample() method to pick a specific number of unique elements from a list. 
Specify how many elements to pick each time.'''
g = random.sample(mylist, 4)
print(g)

'''The choices() method will pick a specific number of elements from a list, just as was shown above. 
However, this time, the elements are not necessarily unique. You use the "k" argument to specify how many elements to pick each time.'''
h = random.choices(mylist, k=2)
print(h)

# You may shuffle elements in a list using the shuffle() method.
random.shuffle(mylist)
print(mylist)

# Secrets module for rando numbers (used for security purposes).
import secrets

# Print a random integer from 0 to 10
i = secrets.randbelow(10)
print(i)

# Print random number of bits. 4 would equal any random integer between 0 and 15.
j = secrets.randbits(4)
# 1111
print(j)

# Print a random element from a list.
mylist2 = list("ABCDEFGH")
k = secrets.choice(mylist2)
print(k)

# NumPy module for random numbers.
import numpy as np

# Print 3 random floats in a 1x3 array.
l = np.random.rand(3)
print(l)

# Print 3 random floats in a 3x3 array.
m = np.random.rand(3,3)
print(m)

# Print random integers in a range. Range below is 0 to 10 with a 3x4 array.
n = np.random.randint(0, 10, (3, 4))
print(n)

# Randomly shuffle elements in an array, only shuffling the first column in the list of arrays.
o = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(o)
np.random.shuffle(o)
print(o)

# To continuously print the same output from a random numbers method, use the seed() method.
np.random.seed(1)
print(np.random.rand(3,3))
# Now run the same blok of code in order to get the same output back.
np.random.seed(1)
print(np.random.rand(3,3))
# Note: a seed generator exists in the secrets module as well, but it behaves a bit differently.