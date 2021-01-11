# Regular print statement:
print("Hello World")

# Drawing a shape:
print("  /|")
print(" / |")
print("/__|")

# Using variables to print different things:
character_name = "Bill"
character_age = "63"
print("I have a friend named " + character_name + ", ")
print("and his age is " + character_age + ".")

# Variables in quotes are strings and you can change them to update the program in the middle of it:
character_name = "Jack"
character_age = "76"
print("I have a friend named " + character_name + ", ")
print("and his age is " + character_age + ".")

# Other types of variables like a number and a Boolean value:
character_age2 = 65
is_male = True

# This will print something out on a separate line:
print("This is \nfun")

# This will print a quotation mark:
print("Print a quotation mark in the middle of this string please\" Thanks")

# Use a string variable to print a statement:
phrase = "Good day"
print(phrase)

# Concatenate a string variable:
print(phrase + " mate")

# Use functions with strings; this makes the string variable lower case:
print(phrase.lower())

# This makes it upper case:
print(phrase.upper())

# This checks if it is written in all upper case and gives you back an answer in a Boolean format:
print(phrase.isupper())

# But now if we convert to upper case and then check again, we'll get a True value back:
print(phrase.upper().isupper())

# Figure out the length of the string by number of characters:
print(len(phrase))

# Specify the exact character in the string that you want to print:
print(phrase[0])
print(phrase[1])
print(phrase[2])
print(phrase[3])

# Use the index function to tell where a character is in a string variable (this is called "passing a parameter"):
print(phrase.index("G"))
print(phrase.index("o"))
print(phrase.index("d"))
print(phrase.index("a"))

# Now I can also use the index function to see at what position a certain word in the string variable started. So, as we can see here, the word "day" started at ordinal number 5:
print(phrase.index("day"))

# You can replace words or letters in a string as well:
print(phrase.replace("Good", "Bad"))
print(phrase.replace("G", "H"))
# Google some more functions and play around with them, there are many out there!

# Let's work with some numbers and see what happens:
print(2)
print(2.0897)
print(-2.0897)
print(3 + 4.5)
print(3 * 4 + 5)
print(3 * (4 + 5))
print(20 / 5)
print(17 - 6)

# 10 divided by three with the remainder (this is called the modulus operator):
print(10 % 3)

my_num = 5
# This will print the number as a string:
print(str(my_num) + " is my favorite number")

# Absolute value of a number:
my_num = -5
print(abs(my_num))

# This function allows a number to be raised to the power of something:
print(pow(4, 6))

# Max returns the larger of the two numbers we pass into it:
print(max(4, 6))

# Can do the same with the smallest number:
print(min(4, 6))

# Can round a number as well:
print(round(2.5))
print(round(3.7))

# Can import external code into our files using import (this will grab a few different math functions from the math module that we can use):
from math import *

# Floor method grabs the lowest number, or rounds down, if you will (in this case it will remove the decimal point):
print(floor(3.7))

# Ceil method does the exact opposite, it rounds up:
print(ceil(3.7))

# This will return the square root of a number:
print(sqrt(36))

# Get input from a user:
input("Enter your name: ")

# Now, let's store the input from our user into a variable:
name = input("Enter your name: ")
print("Hello " + name + "!")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age + ".")

# Time to build a calculator:
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2
print(result)

# Whoops! That just converted everything into a string. We don't want that, we want to add things up. Let's fix it. Let's convert the strings to numbers:
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

# Now this will print an integer (a whole number):
result = int(num1) + int(num2)
print(result)

# But what about decimals? Let's try it:
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print(result)

# Now let's build a mad libs game:
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

# Let's try one more:
man = input("Enter a man's name: ")
food_item = input("Enter a food item: ")
noun = input("Enter a noun: ")
exclamation = input("Enter an exclamation!: ")

print("I knew a man named " + man + ",")
print("He loved to eat " + food_item + ".")
print("When he would sit on the " + noun + "," )
print("he would scream the word: " + exclamation + "!")

# Let's work with some lists. Let's put some friends in our lists array:
friends = ["Kevin", "Karen", "Jim"]

#This will just print the list:
print(friends)

# But let's try to print a specific element in the list using list indexing. Remember, in Python the first index value is 0..then 1, 2, 3 and so on. So, the 1st element in the list is index position 0:
print(friends[0])
print(friends[2])

# You can also index starting from the end of the list instead of the beginning. This will immediately print the last element in the list (keep in mind it actually STARTS with -1, not 0!):
print(friends[-1])

# This will grab all of the elements in index position 1 and everything after that:
print(friends[1:])

# You can also specify a range. This will print all the names from Karen to Oscar:
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends[1:4])

# Let's modify some elements. Let's change Karen to Mike by updating the 2nd element in our list, which corresponds to index value 1:
friends[1] = "Mike"
print(friends[1])

# You can put strings, numbers or Boolean values into a list:
friends = ["Kevin", 2, False]
print(friends)

# Extend a list to another list:
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
print(friends)

# Append another item onto the end of a list:
friends.append("Creed")
print(friends)

# Add another element anywhere in the list based on index value:
friends.insert(1, "Kelly")
print(friends)

# Remove an element in the list:
friends.remove("Jim")
print(friends)

# Remove all elements in the list:
friends.clear()
print(friends)

# Pop an item off of the end of the list:
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop()
print(friends)

# Check for a certain element, item or value in the list:
print(friends.index("Oscar"))
print(friends.index("Kevin"))
# If you put an element, item or value that isn't in the list, Python will throw an error.

# Count how many times the element, item or value appears in the list:
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
print(friends.count("Jim"))

# Sort the list in alphabetical order or in ascending order if it is numbers:
friends.sort()
print(friends)
lucky_numbers.sort()
print(lucky_numbers)

# Reverse a list:
lucky_numbers.reverse()

# Copy a list:
friends2 = friends.copy()
print(friends2)

# Tuple (they are immutable, meaning you cannot modify them at all, use them for when data doesn't ever need to be changed in your program):
coordinates = (4, 5)
print(coordinates[0])
print(coordinates[1])
coordinates2 = [(6, 7), (8, 9), (10, 11)]
print(coordinates2[2])
print(coordinates2[1])

# Functions (code inside the function MUST be indented, outside indentation = outside of the function):
def say_hi():
    print("Hello user")
# Now we have to call the function:
say_hi()

# Let's look at how the flow goes using simple print statements, then the function. It will start at the first print statement, execute the code within the function, then end in the final print statement:
print("Top")
say_hi()
print("Bottom")

# Let's make the function a little bit more powerful by giving it some additional information called a parameter:
def say_hi(name):
    print("Hello " + name)

say_hi("Mike")
say_hi("Steve")

# ^As you can see here, we can give the function a parameter, and based on what parameter we give it, it will perform its task a little bit differently. Let's try one more:
def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))

say_hi("Mike", 35)
say_hi("Steve", 70)
# You can pass in strings, integers, Booleans, arrays, etc. in functions. Generally, you will be breaking your code up into different functions as you go along. This is typical for Python.

# Return statement to return information from a function. We are asking the program to give us some information back from this function, specifically we are asking it to cube the number 3. Let's cube the number and use our return statement:
def cube(num):
    return num*num*num

print(cube(3))
print(cube(4))
# Here's another way to do it. We'll ask that the result of the function be printed:
def cube(num):
    return num*num*num

result = cube(4)
print(result)
# Return statements break you out of the function. So you cannot put anything after it and expect a result. Again, return statements are great for getting values back from a function.

# IF statements to make decisions:
is_male = True
# ^Changing this to false will obviously effect the outcome of the below print statements.
if is_male: 
    print("You are a male")
# The above stetament would print because it is True. If we changed is_male to False, then nothing would print, it would just be blank.
else:
    print("You are not a male")
# The above statement would print because it is not True.

is_tall = True
# ^Changing this to false will obviously effect the outcome of the below print statements.
if is_male or is_tall: 
    print("You are a tall male")
else:
    print("You are neither male nor tall nor both")

# Putting something in parentheses gives it the opposite effect.
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall")
# Try some more of these!

# Using comparisons with IF statements:
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(3, 4, 5))
# You can play around make comparisons with any data type, numbers, strings, Booleans, etc. and you can use many different comparison operators to play around with (>, <, !=, ==, >=, <=). Maybe try some more below?

# Building a better calculator! We'll get 2 numbers and an operator from the user then we will perform the operation:
num3 = float(input("Enter first number: "))
op = (input("Enter operator: "))
num4 = float(input("Enter first number: "))

if op == "+":
    print(num3 + num4)
elif op == "-":
    print(num3 - num4)
elif op == "/":
    print(num3 / num4)
elif op == "*":
    print(num3 * num4)
else:
    print("Invalid operator!")

# Let's learn about dictionaries now. It's a special structure in Python that allows us to store information in what's called key value pairs. You can create a bunch of different key value pairs and when you want to access a specific piece of information inside the dictionary, you can refer to it by its key.
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
# On the left is the key and on the right is the value. These are key value pairs. Keep in mind that each value is unique, so you cannot use the same value twice.
# There are two ways to print the keys here:
print(monthConversions["Nov"])
# or
print(monthConversions.get("Nov"))
# If you print a key that's not mappable to any values in the dictionary, you can actually pass in a default value if you'd like.
# You can also use numbers, etc. doesn't always have to be a string.

# While loops! Structure in Python which allows us to loop through and execute a block of code multiple times. You can loop through a block of code in a while loop as long as a condition is true, if you want. In this case "i" is the condition we are using.
i = 1
while i <= 10:
    print(i)
    i += 1
# ^The operator += here means that the i = i + 1. This is a shorthand way of saying this.
print("Done with loop")
# So what is happening here is we are printing out the while condition/declaration as long as it is true, the moment it becomes false, we print out statement here at the end. The code will keep executing from the top until the while declaration becomes false.
# As you can see, we keep adding 1 to i until we get to the end, so this should print out a series of numbers from 1 to 10 and the loop will stop iterating.

# Building a guessing game:
secret_word = "giraffe" # Secret word variable
guess = "" # Empty guess variable
guess_count = 0 # Starting point for guessing the secret word
guess_limit = 3 # Limit for amount of times the user can guess
out_of_guesses = False # If this variable if equal to False then the user still has more guesses left.

while guess != secret_word and not(out_of_guesses): # If they haven't guessed the word and they still have guesses left, keep looping.
    if guess_count < guess_limit: # If they haven't guessed 3 times yet, keep looping.
        guess = input("Enter guess: ") # User input variable
        guess_count += 1 # Increment guesses by 1 until you've reached the end of the game.
    else:
        out_of_guesses = True # If this variable is True, then the user is out of guesses. If the user is out of guesses then stop looping.

if out_of_guesses: # If the user is out of guesses, print the below statement:
    print("Out of guesses, YOU LOSE!")
else: # Else if the user guessed the word within the allotted amount of guesses, print the below statement:
    print("You win!")

# Let's now cover using for loops! It's a special type of loop in Python that allows us to loop over different collections of items (arrays, letters inside of a string, a series of numbers, etc.). When you specify the name for the for loop variable (like "for ___") it can be any name you want. Below are some simple examples:
# Loop through all the letters in a string and print them:
for letter in "Giraffe Academy":
    print(letter)
# Loop through an array and print it:
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)
# Loop through a series of numbers and print them (this will print numbers 0-9):
for index in range(10):
    print(index)
# This will print every number from 3-9:
for index in range(3, 10):
    print(index)
# Get the length of the array and print it (this, too, will print the elements in the array):
friends = ["Jim", "Karen", "Kevin"]
for index in range(len(friends)):
    print(friends[index])
# Loop through a range and print only the first iteration, otherwise print "Not First":
for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not First")

# Using the exponent function:
print(2**3) # This is 2 cubed

# Let's use this within a for loop:
def raise_to_power(base_num, pow_num):
    result = 1 
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(3, 4))

# List within a list (let's create a grid with 4 rows and 3 columns):
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# Using the ordinal position or index position of the number within the grid, we can print it out:
print(number_grid[0][0])
print(number_grid[2][1])

# Use a nested for loop to parse through the 2D list or array:
for row in number_grid:
    for column in row:
        print(column)

# Build  a basic translator by taking in a string and translating it into a different language:
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

# Comments can be written like this OR 
'''Like this''' # This is called a docstring.

# Catching errors in Python with the try-except block:
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError: # Notice how this is a specific error, the "ValueError" that's built into Python. You always want to be specific with the errors you use in your except block. Another example is the "ZeroDivisionError" which you can throw if divide by zero happens in your code. Look up more specific errors online if you want. 
    print("Invalid input, please enter a number only.")

# Python read command to read a file that is stored outside your Python file (using a try-except block here because we are not actually reading from this file, this is just an example):
try:
    employee_file = open("employees.txt", "r")
# Check to make sure that the file is actually readable (this will return a Boolean value):
    print(employee_file.readable())
# Print out all the contents of the file:
    print(employee_file.read())
# Print an individual line in the file, starting with the first line:
    print(employee_file.readline())
    print(employee_file.readline())
# Print all lines in the file within a list:
    print(employee_file.readlines())
# Index the list to print out only specific lines from the file:
    print(employee_file.readlines()[1])
# For loop it so you can loop through all the lines:
    for employee in employee_file.readlines():
        print(employee)  
# You always have to close the file after you open it:
    employee_file.close()
except:
    print("There is no such file, but nice try!")

# Python append and write command to append or write to an external text file:
try:
    employee_file = open("employees.txt", "a")
# Now actually append the message to the end of the text file:
    employee_file.write("Toby - Human Resources") # Keep in mind that if you want to add this to a new line you need to use the escape character of "\n" to start a new line.
# Always be sure to close the file after working with it, since Python will not do this on its own:
    employee_file.close()
except:
    print("There is no such file, but nice try!")
# Now let's write to the file to change it/overwrite it entirely:
try:
    employee_file = open("employees.txt", "w")
# Now let's make our change to the file:
    employee_file.write("Kelly - Customer Service")
# And always remember to close it:
    employee_file.close()
except:
    print("There is no such file, but nice try!")
# You can actually create an entirely new file using the write command as well.

# Keep in mind how to import modules using the import method, for anything that's not built into the standard Python library, you can pip install it then import it into your code.

# Let's look at classes and objects. These are basically "data types" which can be used to store information about something (more so than just your regular string, integer or Boolean value). First of all, the class defines the object (Student class below), then the object is the data type in action (an actual student). Let's look into it deeper:
class Student: # Let's define what our student is by using functions and attributes:
    def __init__(self, name, major, gpa, is_on_probation): # This is the initialize function that will map out what attributes a student will have. We will pass in attributes into the parentheses. So within this initialize function we have defined what a student is based on different attributes that we have come up with. Now, below we will furter define those attributes through the use of self variables:
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
# Now, before we move on, if I want to import this into another .py file I could say "from scratch import Student". First you define the .py file you are referencing then you refer to the Student class which resides inside of that file. We won't do that here since we are already in the scratch.py file, but you get the idea. Now, let's move on.
student1 = Student("Jim", "Business", 3.1, False) # Now we have created the student1 object which is an instance of the Student class and we have now passed in values into this object by first referencing the class then putting strings, integer and Boolean value within the parentheses to complete the object. Every attribute we defined is now being used within the student1 object (which again is an instance of the Student class.)
print(student1.name) # By using dot notation, I can reference a specific attribute within my student1 object and I can print only that value contained within that attribute rather than printing all the attributes contained in the student1 object.
print(student1.gpa)

student2 = Student("Pam", "Art", 2.5, True)
print(student2.major)
print(student2.is_on_probation)

# My class :):
class Elyscia:
    '''Define my baby'''
    def __init__(self, height, weight, hair_color, eye_color, is_beautiful):
        self.height = height
        self.weight = weight
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.is_beautiful = is_beautiful

baby = Elyscia("5 foot 3", 105, "brown", "brown", True)
print("What are Elyscia's features, like height, weight, hair color and eye color? " + "Oh, and is she beautiful, True or False?")
print(baby.height)
print(baby.weight)
print(baby.hair_color)
print(baby.eye_color)
print(baby.is_beautiful)

# Creating a multiple choice quiz using the import of a class, lists, a function, a for loop, an if statement and a print statement:
from Question import Question # We start by importing our Question class from our Question.py file.
question_prompts = [ # Here we are creating a list of questions and naming it question_prompts.
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
# Here we are creating another list (this time called questions) and adding the Question class and passing in values to the attributes of the Question class. We are first passing in our question prompts and call out which index position they are in within our question_prompts list, then we are giving the correct answer to the question using a string value.
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]
# Now we are defining our run_test function and passing the questions variable (which is a list of question using the question class and question_prompts variable) into it and we are also giving a starting point for our score (which is 0), then we are iterating or looping through each question in the questions variable/list and stating that if the answer that the user inputs within the question prompt attribute (inside of the Question class) is equal to the answer attribute that we have defined within our Question class, then increment their score up by one. Finally, print a statement telling the user how many questions they got correct and then finally run the function to make this program work.
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")

run_test(questions)

# Class functions are functions that we can use inside of a class to modify the objects of the class or give us specific information about the objects:
class Employee: # You could obviously import this class from another file or module, but for now we are just defining it within our local file here.
    def __init__(self, name, job_title, score):
        self.name = name
        self.job_title = job_title
        self.score = score
    
    def is_in_good_standing(self): # This is our class functions (or object function). Though it is small, it provides a service to the class and is very handy.
        if self.score >= 80:
            return True
        else:
            return False

employee1 = Employee("Jim", "engineer", 75)
employee2 = Employee("Michael", "salesman", 80)

print(employee1.is_in_good_standing())
print(employee2.is_in_good_standing())

# Inheritance:
from Chef import Chef # We've created a Chef class and within that class we have used functions to define the different things that the chef can do. But what if we wanted to make a special Chinese chef who can (a) do everything that the regular chef can do and (b) also perform additional functions? This is where we will begin to add inheritance. 
from ChineseChef import ChineseChef
myChef = Chef() # We are just using the regular Chef class here and showing how we can run it.
myChef.make_chicken()
myChef.make_salad()
myChef.make_special_dish()

myChineseChef = ChineseChef() # Now we are using our new ChineseChef class here and inheriting everything from the Chef class yet also changing some things about the Chef class to make them lineup with a Chinese dish, and also adding new functionality on top of the original Chef class functionality.
myChineseChef.make_chicken()
myChineseChef.make_special_dish()





















