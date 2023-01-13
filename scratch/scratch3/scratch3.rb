# Simple print statements
# puts prints something on a new line
# print prints something on the same line
puts "It's time to learn Ruby."
puts "Okay, I'm ready."
print "Are you sure?"
print " Yes, I am sure." 
# ^Notice how a whitespace was added in front here
# If we didn't do this, then there would no space between 
# the two print statements
puts ""

# Drawing a shape
puts "   /|"
puts "  / |"
puts " /  |"
puts "/___|"

# Variables
character_name = "Jim"
character_age = "42"
fruit = "apples"
vegetable = "cabbage"
# Notice that when adding variables to our story we
# have to make sure that we put prentheses around the
# puts statements
puts ("There was a man named " + character_name)
puts ("he was " + character_age + " years old.")
puts ("He really liked " + fruit)
puts ("but he didn't like " + vegetable + ".")
# Now let's update our variables to change the story!
character_name = "Billy Bob"
character_age = "36"
fruit = "bananas"
vegetable = "spinach"
puts ("There was also a man named " + character_name)
puts ("he was " + character_age + " years old.")
puts ("He really liked " + fruit)
puts ("but he didn't like " + vegetable + ".")

# Data types
string = "Jack" # string
integer = 62 # integer
floating_point = 3.2 # floating point number
boolean = true # Boolean
boolean2 = false # Boolean
none = nil # nil (means no value)

# Strings in Ruby
puts "mrichinfinite"
# Quotation marks within a string
puts "\"I like cheese.\""
# New line within a string
puts "I love to\ndrink milk"
# Using a variable
phrase = "Let's have fun with Ruby"
puts phrase

# String methods:

# Change everything to uppercase and then to lowercase
puts "Ruby programming".upcase()
puts "Ruby programming".downcase()
puts phrase.upcase()
puts phrase.downcase()
# Remove whitespace from a string
phrase2 = "     All this whitespace needs to go     "
puts phrase2.strip()
# Display how many characters are inside of a string
puts phrase.length()
puts phrase2.length()
# Check to see if something is inside of a string
puts phrase.include? "Ruby"
puts phrase.include? "wow"
puts phrase2.include? "whitespace"
puts phrase2.include? "no way"
# Check to see which character is at which index position in a string
puts phrase[0]
puts phrase2[11]
puts phrase[2]
puts phrase2[10]
# Print a range of characters
puts phrase[0,3]
puts phrase[11,16]
puts phrase2[6,9]
puts phrase2[7,10]
# Check to see at what index position a character resides
puts phrase.index("h")
puts phrase2.index("w")
# Check to see at what index position a string of characters begins
puts phrase.index("Ruby")
puts phrase2.index("whitespace")

# Google more string methods in Ruby!

# Numbers + math
puts 67
puts 3.14
puts -5.9678
puts 5 + 9
puts 10 - 7
puts 7 * 7
puts 81 / 9
puts 2**3 # exponent
puts 10 % 3 # modulus (divides then prints remainder)
# Using math in a variable
num = 20
puts num / 5

# Useful methods:

# How to print a number when combining it with a string
# (You must do it this way to avoid an error)
puts (num.to_s + " is the best number ever!")
# Print the absolute value of a number
puts num.abs()
# Round a number
num2 = 36.67898
puts num2.round()
# Print the next highest number than the one given
puts num2.ceil()
# Print the next lowest number than the one given
puts num2.floor()
# Using the Math class to get the square root of a number
puts Math.sqrt(40)
puts Math.sqrt(num2)
puts Math.log(1) # logarithm
# Keep in mind that when you perform math operations
# in Ruby, integers will only return integers, however
# using floating point numbers will return floating 
# point numbers (unless you're using the Math class)

# Google more math operations in Ruby!

# Getting user input
puts "Enter Your Name: "
name = gets 
puts ("Hello " + name)
# If you want to add additional text after the name variable
# without Ruby creating a new line, use the chomp() method
puts "Enter your age: "
age = gets.chomp()
puts ("You are " + age + " years old!")

# Building a basic calculator
puts "Enter a number: "
num1 = gets.chomp()
puts "Enter another number: "
num2 = gets.chomp()
puts (num1 + num2)
# ^Notice how this printed out, it concatenated the two strings 
# (which were num1 and num2), but that's not what we want, we
# want to add num1 and num2 together and get a result

# So, let's try this a different way
puts (num1.to_i + num2.to_i)
# ^This will convert the strings in these two variables to integers

# Now that's helpful for integers, but this won't work for decimal 
# numbers

# We need to do this for decimal numbers (floating point numbers)
puts (num1.to_f + num2.to_f)

# The other way to do it is like this (I think this is cleaner)
puts "Enter a number: "
num1 = gets.chomp().to_f
puts "Enter another number: "
num2 = gets.chomp().to_f
puts (num1 + num2)

# Build a mad libs game
puts "Enter a color: "
color = gets.chomp()
puts "Enter a plural noun: "
plural_noun = gets.chomp()
puts "Enter a celebrity name: "
celebrity_name = gets.chomp()

puts ("Roses are " + color)
puts (plural_noun + " are blue")
puts ("I love " + celebrity_name)

# Arrays
friends = Array["Kevin", "Karen", "Oscar"]
puts friends
# Arrays can contain different data types other than just strings
data = Array[1, "Karen", false]
puts data
# Access an element inside of an array
puts friends[1]
puts data[0]
# Access an element from the end of an array
puts friends[-1]
puts data[-2]
# Access a range of elements (in this example, only the
# elements with index position 0 and 1 will actually print)
puts friends[0, 2]
# This would print all the elements in our friends array
puts friends[0, 3]
# Let's try one more
puts data[0, 1]
# Modifying elements inside of an array is easy
friends[0] = "Bill"
data[2] = true
# Create a new array but define the elements within it later on
colors = Array.new

colors[0] = "blue"
colors[1] = "red"
colors[6] = "yellow"
# Now, notice when I print this, the empty elements are printed as well
puts colors

# Useful array methods
# How many elements in the array?
puts friends.length()
# Does the array include this specified element?
puts friends.include? "Karen"
# How about this one?
puts friends.include? "Marty"
# Reverse the order of the array
puts friends.reverse()
# Sort the array alphabetically (only works with similar data types)
puts friends.sort()
# So, we can do it with integers too
numbers = Array[3, 2, 1]
puts numbers.sort()

# Hashes (they are just like dictionaries, they define key value pairs)
states = {
    "New York" => "NY",
    "Texas" => "TX",
    "California" => "CA"
}
puts states
# So as you can see, we have key value pairs here,
# let's just print a key and return the value
puts states["Texas"]
puts states["California"]
# Some other ways to define key value pairs
state = {
    :Michigan => "MI",
    1=> "MI"

}
puts state[:Michigan]
puts state[1]

# Methods (execute a block of code that's callable at a later time)
def sayhi
    puts "Hello User"
end # Must put this here to close the method

sayhi # This will print "Hello User"

# Now let's pass in some input parameters/arguments to see how it works
def sayhello(name, age)
    puts("Hello " + name + ", you are " + age.to_s) # Remember to put .to_s to avoid an error
end
# Be sure to put the right number of arguments in here (need one for name and one for age)
sayhello("Billy Bob", 95)

# You can assign default values to input parameters/arguments
def saysomething(name="Joe", age=42)
    puts("Hello " + name + ", you are " + age.to_s)
end
# So now, since we have already defined default values for our arguments, we don't have to put them here again
saysomething

# Return statements (the return keyword signals to Ruby that we are DONE with the method
# therefore, no further code will be executed after the return statement)
def cube(num)
    return num * num * num
    # So now, this will not print anything
    puts "Hello"
end

puts cube(2)

# You can return multiple values in a return statement
def squared(num)
    return num * num, 64, "Hello"
end

puts squared(3)

# You can also access each element in a return statement array by calling its index position
puts squared(2)[1]
puts squared(6)[2]

# If Statements
isanimal = true
islarge = true

if isanimal and islarge
    puts "You are a large animal!"
elsif isanimal and !islarge # This exclamation point is called a negation operator, it means "is not"
    puts "You are a small animal!"
elsif !isanimal and islarge
    puts "You are not an animal, but you are large!"
else
    puts "You are not an animal, and you are not large!"
end

isanimal = true
islarge = false

if isanimal and islarge
    puts "You are a large animal!"
elsif isanimal and !islarge
    puts "You are a small animal!"
elsif !isanimal and islarge
    puts "You are not an animal, but you are large!"
else
    puts "You are not an animal, and you are not large!"
end

isanimal = false
islarge = true

if isanimal and islarge
    puts "You are a large animal!"
elsif isanimal and !islarge
    puts "You are a small animal!"
elsif !isanimal and islarge
    puts "You are not an animal, but you are large!"
else
    puts "You are not an animal, and you are not large!"
end

isanimal = false
islarge = false

if isanimal and islarge
    puts "You are a large animal!"
elsif isanimal and !islarge
    puts "You are a small animal!"
elsif !isanimal and islarge
    puts "You are not an animal, but you are large!"
else
    puts "You are not an animal, and you are not large!"
end

# Create a method called max that uses if statements to return the largest number
# when 3 numbers are passed into it
def max(num1, num2, num3)
    if num1 >= num2 and num1 >= num3
        return num1
    elsif num2 >= num1 and num2 >= num3
        return num2
    else
        return num3
    end
end

puts max(1, 2, 3)
puts max(20, 54, 9)
puts max(92, 46, 71)
# Here we used comparison operators to compare different values that resulted in a Boolean value
# We can use this instead of having hard coding a Boolean value beforehand

# Building a better calculator
puts "Enter first number: "
num1 = gets.chomp().to_f # Convert string to floating point number 
puts "Enter first operator: "
op = gets.chomp()
puts "Enter second number: "
num2 = gets.chomp().to_f

if op == "+"
    puts (num1 + num2)
elsif op == "-"
    puts (num1 - num2)
elsif op == "*"
    puts (num1 * num2)
elsif op == "/"
    puts (num1 / num2)
else
    puts "Invalid operator, please enter a valid operator."
end

# Case expressions. We can use these in lieu of if statements in certain situations
def get_day_name(day)
    
    day_name = ""

    case day
    when "mon"
        day_name = "Monday"
    when "tue"
        day_name = "Tuesday"
    when "wed"
        day_name = "Wednesday"
    when "thu"
        day_name = "Thursday"
    when "fri"
        day_name = "Friday"
    when "sat"
        day_name = "Saturday"
    when "sun"
        day_name = "Sunday"
    else
        day_name = "Invalid abbreviation"
    end
    return day_name
end

puts get_day_name("thu")
puts get_day_name("wed")
puts get_day_name("sun")
puts get_day_name("cat")

# While loops
index = 1
while index <= 5
    puts index
    index += 1
end

# Building a guessing game (user tries to guess a secret word)

# Define secret word
secret_word = "fun"
# User input
guess = ""
# Starting number of guesses user has made
guess_count = 0
# Limit of guesses user has before they lose the game
guess_limit = 3
# Initial Boolean value for whether user is out of guesses or not
out_of_guesses = false

# Now create a while loop that continues to iterate, asking the user for input

# While the user input does not equal the secret word and the user is not out of guesses
# continue iterating through the while loop
while guess != secret_word and !out_of_guesses
# If the guess count is less than the guess limit, allow the user to input a guess
    if guess_count < guess_limit
        # User input
        puts "Enter your guess: "
        # Prevent creation of a new line during user input
        guess = gets.chomp()
        # Increment guess count by 1 until limit is reached
        guess_count += 1
    else
        # When limit is reached, user is out of guesses, define secondary Boolean value
        out_of_guesses = true
    # Remember to close out if statement and while loop with "end"
    end 
end

# Messages when user is out of guesses vs. when they guess the secret word
if out_of_guesses
    puts "You Lose!"
else
    puts "You Win!"
end

# For loops 
# Loop/iterate through a collection of elements

# Create an array
friends = ["Billy", "Bob", "Kaylee", "Susan"]

# Just FYI, you can print a specific index position from an array this way
puts friends[1]

# Use a for loop to iterate through the friends array
# During each iteration of "friend", a different friend in the array will be outputted
# "Friend" can be any name that you desire, it helps if it adds context though, that's why we use "friend" here
for friend in friends
    # Print the iteration
    puts friend
end

# A second way of for looping in Ruby, again "friend" can be anything you want
friends.each do |friend|
    puts friend
end

# Loop/iterate through a block of code for a specified number of times
# Shown below is how to iterate through a series of numbers, in this case it is 0 to 5
# "Index" can be any name that you desire
for index in 0..5
    puts index
end

# A second way of the above example is shown below, again "index" can be anything you want
6.times do |index|
    puts index
end

# Exponent method (FYI, will only work with positive numbers)
def power(base_num, power_num)
    result = 1
    # Loop through the code block x number of times where x is power_num
    power_num.times do #|index| <-- This is optional
        result = result * base_num
    end
    return result
end

# First, we will try 2, cubed
puts power(2, 3)
# Now, let's try 5, squared
puts power(5, 2)
# Finally, let's try 7 to the power of 10
puts power(7, 10)

# A note on comments

=begin
I can make multiline comments using =begin and =end, however
using hastags (#) is the most typical way
# Just like this
# and this
# and this
# Thanks!
=end

# Reading from files

# Open the specified file, read into it and put the contents into a variable
File.open("employees.txt", "r") do |file|
# Since this file is in my current directory I don't need to specify the path, 
# but if it was not in my current directory, I would need to specify a file path

# Print the file metadata (how it's stored in Ruby)
puts file
# Print the file's contents
puts file.read
# See if something exists within said file or not
puts file.read().include? "Bill"
end

# Another way of doing the same thing as above
file = File.open("employees.txt", "r")
# Loop through all the lines in the file and then print it
for line in file.readlines()
    puts line
end
# We always want to close files after opening them or else they remain open and consume memory in our program
file.close()

# Writing to files (append something to a file, modify a file, overwrite an entire file or create a new file)

# Append something to the file
File.open("employees.txt", "a") do |file|
    # Add this to a new line in the file
    file.write("\nBobby, Engineering")
end

file.close()

# Overwrite entire file
File.open("employees.txt", "w") do |file|
    file.write("No more employees!")
end

file.close()

# Create a new file (let's create a new HTML file)
File.open("index.html", "w") do |file|
    file.write("<h1>Hello World!</h1>")
end

file.close()

# Read and write to a file
File.open("employees.txt", "r+") do |file|
    # Move cursor in file character by character
    file.readchar()
    file.write("X")
    # Move cursor in file line by line
    file.readline()
    file.write("\nThe second line of the file is now changed.")
end

file.close()

# Exception handling

# For example, create an array
lucky_nums = [4, 6, 8, 12, 14, 16, 18]
# In a begin block, create a bad call on the array
begin
    lucky_nums["cat"]
# In a rescue block, state the type of exception it is and point it to 
# a variable with a name of your choice (here we are simply using "exception" here)
rescue TypeError => exception
    # Put any code you want, but make sure to call on your variable at some point
    puts "Wrong type"
    puts exception
end
# Try it again but with a different exception this time
begin
    num = 10 / 0
rescue ZeroDivisionError => exception
    puts "Division by zero error"
    puts exception
end

# Classes and objects
class Book 
    # Define what a "book" entails in your program
    attr_accessor :title, :author, :pages
end

# Create book objects (object is an instance of a class)
book1 = Book.new()
book1.title = "My Random Book"
book1.author = "Anonymous"
book1.pages = 500

# Print the attributes of the book we created
puts book1.title
puts book1.author
puts book1.pages

book2 = Book.new()
book2.title = "Another Random Book"
book2.author = "Anonoymous #2"
book2.pages = 900

puts book2.title
puts book2.author
puts book2.pages

# Everything is an object in Ruby!
