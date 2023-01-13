# Sets: unordered, mutable, no duplicates
myset = {1, 2, 3}
print(myset)
# Remember that no duplicates will display. See below.
myset = {1, 2, 3, 1, 2, 3}
print(myset) # As you can see it still printed out just like the myset variable did.

# You can use the set() function to create a set out of something else (we'll use a list here).
myset = set([1, 2, 3])
print(myset)
# However, if you do the same thing with a string, it's going to look a bit different.
myset = set("Hello")
print(myset)
# To print an empty set you must use the set() function.
myset = set()
print(myset)
# To add or remove elements from a set use the add() and remove() methods.
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)
myset.remove(1)
myset.remove(2)
print(myset)
'''Another way to remove elements without potentailly encountering any errors (like
if you specify an element that doesn't exist in the set) is to use the discard() method.'''
myset.discard(3)
print(myset)
'''You can also remove the first element in a set with the pop() method. This will print 
out which element was removed then will print the new set with the removed element.'''
myset = {1, 2, 3}
print(myset.pop())
print(myset)
# Iterate over a set using a for loop (you don't have to use x, you can call it whatever you want).
myset = {1, 2, 3}
for x in myset:
    print(x)
# Use an if statement to check if an element exists in a set.
if 3 in myset:
    print("Yes")
# If the element doesn't exist in the set then nothing is printed.
if 4 in myset:
    print("Yes")

# Combine two sets together without duplication using the union() method.
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens) # Combining odds and evens sets here (without duplication).
print(u)
# Print the duplicates from two sets using the intersection() method.
x = odds.intersection(evens)
print(x) # This will of course print nothing.
y = odds.intersection(primes)
print(y) # But this will print something.
z = evens.intersection(primes)
print(z) # And this will print something.

# Calculate the difference between two sets.
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
# This will only print the elements that are different from the first set.
diff = setA.difference(setB)
print(diff)
# To do it the other way around, do it this way.
diff = setB.difference(setA)
print(diff)
# Let's look at a different difference() method called symmetric_difference().
diff = setA.symmetric_difference(setB)
print(diff) # As you can see, this prints the difference between both sets in one fell swoop!

# This does the same thing.
diff = setB.symmetric_difference(setA)
print(diff)

# Modify a set. This updates a set with another set without duplication.
setA.update(setB)
print(setA)
# This updates setA by removing duplicates and differences found in setB.
setA.difference_update(setB)
print(setA)
# This updates setC by keeping only the duplicates and removing the differences from both sets.
setC = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setD = {1, 2, 3, 10, 11, 12}
setC.intersection_update(setB)
print(setC)
# This updates setE by removing the duplicates found in setF and adding the remainder from both sets.
setE = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setF = {1, 2, 3, 10, 11, 12}
setE.symmetric_difference_update(setF)
print(setE)

# Subset method. Are all the elements in setX also in setY?
setX = {1, 2, 3, 4, 5, 6}
setY = {1, 2, 3}
setZ = {7, 8}
print(setX.issubset(setY))
# Now let's reverse it. Are all the elements in setY also in setX?
print(setY.issubset(setX))

# Superset method. Are all the elements in setY in setX?
print(setX.issuperset(setY))
# Now let's reverse it. Are all the elements in setX also in setY?
print(setY.issuperset(setX))

# Disjoint method. Is setX completely different from setY?
print(setX.isdisjoint(setY))
# What about setZ? Is setX completely different from setZ?
print(setX.isdisjoint(setZ))
# Is setY completely different from setZ?
print(setY.isdisjoint(setZ))

# Copy a set, then add something to the copied set.
setM = {1, 2, 3, 4, 5, 6, 7, 8}

setN = setM
# Here we use the add() method to add something to the set.
setN.add(9)
print(setN)
print(setM) # As you can see, even the original set is changed now. This is because sets are mutable.

# Now let's just make a simple copy of a set using the copy() method.
setO = setM.copy()
print(setO)
# Here's another way to do it using the set() function.
setP = set(setM)
print(setP)

# Frozen set. This makes a set immutable.
v = frozenset({1, 2, 3})
print(v)