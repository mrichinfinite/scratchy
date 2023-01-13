# Lists: ordered, mutable, and allows for duplicate elements.
mylist = ["banana", "cherry", "apple", 5, True, "apple"]
print(mylist)

''' You can reference items in a list by the index position. 
Positive numbers start from the beginning of the list while negative numbers start at the end of the list. 
(Be careful to not specify an index position that is too large or you will get an error stating that the index is out of range!) '''
item = mylist[0]
item2 = mylist[-1]
print(item)
print(item2)

''' You can use the list function to create a new empty list 
(and if you want, you can append items to them as well, which we will look at later) or reference another list. '''
mylist2 = list()
mylist3 = list(mylist)
print(mylist2)
print(mylist3)

# Iterate through a list using a for loop (note that you do not have to use the value of "i" here, it can be "x" or anything you want).
for i in mylist:
    print(i)

# Use simple if statements to see if an item exists inside the list.
if "banana" in mylist:
    print("yes")
else:
    print("no")

if "blackberry" in mylist:
    print("yes")
else:
    print("no")

# Check to see how many items exist within the list.
print(len(mylist))

# Append an item to the end of the list.
mylist.append("lemon")
print(mylist)

# Insert an item into the list by specifying at which index position you want to insert it.
mylist.insert(1, "strawberry")
print(mylist)

# This will return the last item in the list and also remove it from the list.
item3 = mylist.pop()
print(item3)
print(mylist)

''' This will remove a specific item from the list. 
Be careful to not specify an item that is not in the list or you will get a ValueError stating: list.remove(x): x not in list. '''
item4 = mylist.remove("cherry")
print(mylist)

# This will remove all the elements in the list.
item5 = mylist.clear()
print(mylist)

# This will reverse the list order.
mylist4 = ["banana", "apple", "blackberry", 5, False]
item6 = mylist4.reverse()
print(mylist4)

# This will sort a list in ascending order.
mylist5 = [4, 3, 2, 1, -1, -5, 10, -32, 150, 200]
item7 = mylist5.sort()
print(mylist5)

# This will print a brand new sorted list instead of just sorting an already existing list.
new_list = sorted(mylist5)
print(mylist5)

# You can create a new list this way too.
mylist6 = [0] * 5
print(mylist6)

# This will combine 2 lists together and print them as 1 single list.
mylist7 = [1, 2, 3, 4, 5, 6, 7]
new_list2 = mylist7 + mylist6
print(new_list2)

''' Slicing: you can slice a list by indicating the starting index position and the stopping index position 
(again, this is called slicing). '''
mylist8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = mylist8[1:5] 
''' ^Notice how it starts at index position 1 and stops at index position 5, however when we print this it will 
only print the items/values for index positions 1-4. So the stopping index position is actually excluded. '''
print(a)
# Now, if you do not specify a starting index position then it just starts all the way from the beginning.
b = mylist8[:5]
print(b)
# Likewise, if you do not specify a stopping index position then it just stops all the way at the end.
c = mylist8[1:]
print(c) 
''' Now, this will step through a list based on the amount of steps you specify. 
So, the below example starts at the beginning of the list and steps through the list by 2 all the way until the end of the list. '''
d = mylist8[::2]
print(d)
# You can do this in reverse order as well.
e = mylist8[::-2]
print(e)

# This will copy a list.
list_cpy = mylist8.copy()
print(list_cpy)
# This another way to copy a list.
list_cpy2 = list(mylist8)
print(list_cpy2)
# This is a third way to copy a list (using slicing).
list_cpy3 = mylist8[:]
print(list_cpy3)
# Now if I wanted to append something to the end of that copied list, I could do it this way.
list_cpy.append("lemon")
print(list_cpy)

''' List comprehension: create a new list from an existing list with a single line! We will use an expression followed by a for loop to achieve this. 
Again, we do not HAVE to use the value of "i" in the expression, you can call it whatever you want. '''
x = [1, 2, 3, 4, 5, 6, 7]
y = [i*i for i in x] # So all we are doing here is squaring each item in the list and iterating through that list with a for loop.
print(x) # This will print the original list.
print(y) # This will print the new list that we created using our expression + for loop.

# You can see how we can use many of the built-in Python methods and functions to easily create and modify lists!
