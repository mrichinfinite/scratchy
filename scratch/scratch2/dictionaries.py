# Dictionary: Key-Value pairs, Unordered, Mutable
mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

# Another way to create a dictionary.
mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

# Print values by calling the associated key.
value = mydict["name"]
print(value)

value = mydict["age"]
print(value)

value = mydict["city"]
print(value)

# Add a key-value pair to an existing dictionary.
mydict["email"] = "max@xyz.com"
print(mydict)

# This will overwrite the existing value in the previously defined key.
mydict["email"] = "coolmax@xyz.com"
print(mydict)

# Delete key-value pairs from an existing dictionary.
del mydict["name"]
print(mydict)

# Another way to remove key-value pairs from an existing dictionary.
mydict.pop("age")
print(mydict)

# Remove the last key-value pair from an existing dictionary.
mydict.popitem()
print(mydict)

# Check to see if a key exists in an existing dictionary, then print its value.
if "name" in mydict2:
    print(mydict2["name"])

# Another way to check if a key exists in an existing dictionary, then print the result.
try:
    print(mydict2["name"])
except:
    print("Error")

try:
    print(mydict2["lastname"])
except:
    print("Error")

# Loop through the keys in an existing dictionary, then print them out.
for key in mydict2:
    print(key)

# Another way to loop through the keys in an existing dictionary, then print them out.
for key in mydict2.keys():
    print(key)

# You can do the same thing with the values.
for value in mydict2.values():
    print(value)

# Finally, you can do the same with both.
for key, value in mydict2.items():
    print(key, value)

# Copy a dictionary.
mydict2_cpy = mydict2
print(mydict2_cpy)

# Copy a dictionary then modify the original one.
mydict2_cpy["email"] = "max@xyz.com"
print(mydict2_cpy)

# Now check the modified copy.
print(mydict2)

# Another way to copy a dictionary.
mydict2_cpy = mydict2.copy()
print(mydict2_cpy)

# Yet another way to copy a dictionary.
mydict2_cpy = dict(mydict2)
print(mydict2_cpy)

# Update a dictionary, then print the updated dictionary.
my_dict = {"name": "Joe", "age": 27, "city": "San Jose"}
my_dict_2 = dict(name="Bill", age=30, email="bill@bill.com")

my_dict.update(my_dict_2)
print(my_dict)

# Key-value pairs can be any mutable value, we'll use integers below.
my_dict_3 = {3: 9, 6: 36, 9: 81}
print(my_dict_3)

# Again, we'll print a value by calling the associated key (just like we did earlier).
value2 = my_dict_3[3]
print(value2)

# Tuples within dictionaries (FYI, you cannot do this with lists because lists are mutable and not hashable).
mytuple = (8, 7)
my_dict_4 = {mytuple: 15}
my_dict_5 = {15: mytuple}

print(my_dict_4)
print(my_dict_5)