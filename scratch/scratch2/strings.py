# Strings: ordered, immutable, text representation
my_string = "Hello World"
print(my_string)
# Single quotes work just fine as well.
my_string2 = 'This is fun'
print(my_string2)
'''If you need to put an apostrophe in your string,
either use a backslash or keep the string in double quotes'''
my_string3 = 'I\'m a programmer'
my_string4 = "I'm a programmer"
print(my_string3)
print(my_string4)
# Multline strings use similar syntax as multiline comments (can be wrapped in single or double quotes).
string = '''Hello
World'''
print(string)
string2 = """This is
fun"""
print(string2)
# You can make it to where a multiline string still stays on one line though (just use a backslash).
string3 = '''Hello \
World'''
print(string3)
# We can access elements in a string from the beginning or from the end of a string.
char = string3[0]
char2 = string3[-1]
print(char)
print(char2)
# Note: you cannot modify elements within an existing string though (remember they are immutable).

# Slicing. You can slice/print a range of a string using slicing.
substring = string3[1:5]
print(substring)
# This starts at the beginning and ends before the specified index position.
substring2 = string3[:5]
print(substring2)
# This prints the whole string.
substring3 = string3[:]
print(substring3)
# This will also print the whole string.
substring4 = string3[::]
print(substring4)
# This will reverse the string.
substring5 = string3[::-1]
print(substring5)

# Concatenating strings. Simple task using an addition operator.
greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

# Iterate over a string (doesn't have to be "x", can be anything you want).
for x in greeting:
    print(x)

# If statement to determine if an element exists in a predefined string.
if 'e' in greeting:
    print('yes')
else:
    print('no')
# Let's try a different one.
if 'p' in greeting:
    print('yes')
else:
    print('no')
# Let's try a substring and see what happens.
if 'ell' in greeting:
    print('yes')
else:
    print('no')

# Remove whitespace from a string using the strip() method.
this_string = '     Hello World     '
this_string = this_string.strip()
print(this_string)
# Note: you must assign the strip() method to a new variable (like we did above) in order for it to work.

# Convert every character in a string to upper case.
print(this_string.upper())
# Convert every character in a string to lower case.
print(this_string.lower())

# Check if a string starts with a character or series of characters.
print(this_string.startswith('H'))
print(this_string.startswith('Hello'))
print(this_string.startswith('World'))

# Check if a string ends with a character or series of characters.
print(this_string.endswith('H'))
print(this_string.endswith('d'))
print(this_string.endswith('World'))

# Find the index position of a character or substring.
print(this_string.find('o'))
print(this_string.find('lo')) # Starts at index position 3.
# Note: if a substring is not found, a -1 is returned.

# Count the number of characters in a string.
print(this_string.count('o'))
print(this_string.count('p'))

# Replace characters or substrings within a string by printing a new string.
print(this_string.replace('o', 'p'))
print(this_string.replace('World', 'Universe'))

# Convert a string into a list.
string_it = "How are you doing?"
my_list = string_it.split()
print(my_list)
# Note: the delimeter is a space, so the string is split where the spaces are.
# Let's say you were separating elements in a string by a comma instead.
string_it2 = "How,are,you,doing?"
# Then, the delimeter would be a comma.
my_list2 = string_it2.split(",")
print(my_list2)
# Now, let's convert the list back into a string using the join() method.
new_string = ' '.join(my_list2)
print(new_string)
# Note: This method is very useful in general for converting lists into strings (it is also very fast).

# Formatting strings.
# This will print the var variable we defined inside of the stringy variable we defined.
var = "Tom"
stringy = "the variable is %s" % var
print(stringy)
# This will do the same thing but we use %d this time since var2 is an integer.
var2 = 3
stringy2 = "the variable is %d" % var2
print(stringy2)
# For floating point numbers (decimal numbers) we use %f.
var3 = 3.1234567
stringy3 = "the variable is %f" % var3
print(stringy3)
'''If we want to specify how many digits are printed, we can do so by putting the number of digits we 
want to print in front of the f. Be sure to put a dot in front of all of it in order for it to work.'''
var4 = 3.1234567
stringy4 = "the variable is %.2f" % var4
print(stringy4)
# Note: this is a very old formatting style. Let's look at a newer formatting style below.
var5 = 3.1234567
stringy5 = "the variable is {}".format(var5) # We use the format() method here.
print(stringy5)
# If we want to specify a specific number of digits to be printed with the new style, we would do it this way.
var6 = 3.1234567
stringy6 = "the variable is {:.2f}".format(var6)
print(stringy6)
# If we have multiple variables, simply continue using the braces as needed.
var7 = 6
stringy7 = "the variable is {:.2f} and {}".format(var6, var7)
print(stringy7)
# Now, the above style is still old. The VERY newest way of doing all of this (since Python 3.6 and above) is using f-strings.
stringy8 = f"the variable is {var6} and {var7}"
print(stringy8)
# Note: this is much more readable and faster, so this is truly the recommended method moving forward.
# In fact, with f-strings, we can change the value of a variable at runtime. Let's try it.
stringy9 = f"the variable is {var6*2} and {var7}"
print(stringy9)