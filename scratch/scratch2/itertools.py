# itertools: product, permutations, combinations, accumulate, groupby and infinite iterators
from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a, b)
# We'll see that after printing this out, we'll now have a product object.
print(prod)
# To see everything inside that object, print it as a list.
print(list(prod))
'''So as you can see, we are printing the first element in list a, with the first element in list b and again the first element in list a, 
but now with the second element in list b. Then, the second element in list a with the first element in list b and again the second 
element in list a, but now with the second element in list b. So we'll get four tuples printed inside of a list here.'''

# You can repeat how many times a product object gets printed out by doing this.
x = [1, 2]
y = [3]
prod = product(x,y, repeat=2)
print(list(prod))

# Now let's look at permutations. These will return all possible orderings of an input.
from itertools import permutations
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))
# To specify the length of the permutations, do this. 
perm2 = permutations(a, 2) # This would only return two elements in each tuple that's printed out.
print(list(perm2))

# Now, let's take a look at combinations. This function will make all possible combinations with a specified length.
from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
comb = combinations(a, 2) # You must specify this second length argument here. It is mandatory.
print(list(comb))
# Now let's try combinations with replacements. This will print all possible combinations, including repeating numbers.
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

# Time to look at accumulate. This function makes an iterator that returns accumulated sums for a given input.
from itertools import accumulate
a = [1, 2, 3, 4]
acc = accumulate(a)
# First, let's just print list a.
print(a)
# Now, we'll print the accumulated list. 
print(list(acc))
'''So as you can see here, this is what we did: we started with 1, then we added 1 to 2 which equals 3, then we added 3
to 3 which equals 6, then we added 6 to 4 which equals 10. This is how we got our accumulated list.'''

# We can also multiply elements by importing the operator function and adding it to our accumulate function as an additional argument.
import operator
b = [1, 2, 3, 4]
acc2 = accumulate(b, func=operator.mul)
print(list(acc2))
# To keep printing the next number in the list until you get to the highest one, do this.
c = [1, 2, 5, 3, 4]
acc3 = accumulate(c, func=max)
print(list(acc3))
'''So you can see here that the iterator stopped once it got to 5 and kept printing 5 only. This is because it's the highest 
number in the list compared to every other number in this list.'''

# Now, let's look at the groupby function. It makes an iterator that returns keys and groups from an iterable.
from itertools import groupby
# First, let's define a function that returns True if the input is smaller than 3. 
def smaller_than_3(x):
    return x < 3
# Now we'll create a list.
a = [1, 2, 3, 4]
# We'll use our groupby function to iterate over the list and find the elements that are smaller than 3.
group_obj = groupby(a, key=smaller_than_3)
'''For any elements that are smaller than 3 in the list, return the Boolean result for our key argument 
(which is our smaller_than_3 function that we defined earlier) and show us the corresponding values from the list.'''
for key, value in group_obj:
    print(key, list(value))

# To shorten this up a bit, you can just use the lambda function like this (instead of defining a function first).
b = [1, 2, 3, 4]
group_obj2 = groupby(b, key=lambda x: x<3)
for key, value in group_obj2:
    print(key, list(value))

# Let's try this now with a dictionary.
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, {'name': 'Lisa', 'age': 26}, {'name': 'Donna', 'age': 28}]
# Now, let's group each person by age.
group_obj3 = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj3:
    print(key, list(value))

# Let's look at some infinite iterators now. We'll start with count, then move onto cycle and repeat.
from itertools import count, cycle, repeat
# Start counting at 10 and stop counting at 15. If you don't break at a certain number this will return an infinite loop!
for i in count(10):
    print(i)
    if i == 15:
        break
# Cycle. This will cycle infinitely through a list until a stop condition is defined. Here we break at 3.
a = [1, 2, 3]
for i in cycle(a):
    print(i)
    if i == 3:
        break
# Repeat. This will repeat a specified element in the list until a stop argument is defined. In this case we stop after 4 repeats.
a = [1, 2, 3]
for i in repeat(1, 4):
    print(i)