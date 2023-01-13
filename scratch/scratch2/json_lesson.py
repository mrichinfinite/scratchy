import json

# Create a dictionary.
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# Convert it into a JSON string.
person_json = json.dumps(person)

# Use different formatting styles for the JSON string.
person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)

# Print the results as JSON output.
print(person_json) 
print(person_json2)

# Create a JSON file and write to it. Add the person dictionary to the file and indent 4 spaces. 
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

# Convert from JSON string back to Python dictionary.
person3 = json.loads(person_json)
print(person3)

# Read from a JSON file and print the output as Python dictionary.
with open('person.json', 'r') as file:
    person4 = json.load(file)
    print(person4)

# Create a class and encode the custom object in JSON format. There are 3 ways to do this shown below.

# Begin by creating the class.
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# Define a variable for an instantiation of the class.
user = User('Max', 27)

# First way of encoding object in JSON. Start by defining a function.
def encode_user(o):
    # Use the isinstance method and pass in an object and the User class as arguments.
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

# Define variable which returns JSON string, then print the output.
userJSON = json.dumps(user, default=encode_user)
print(userJSON)

# Second way. Start by importing JSONEncoder from the json module.
from json import JSONEncoder

# Create a custom class object and pass in the JSONEncoder.
class UserEncoder(JSONEncoder):
    # Define a function and use self and an object as input parameters.
    def default(self, o):
        # Use the isinstance method again and return the JSON string using the JSONEncoder.
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

# Define variable which returns JSON string, then print the output.
userJSON2 = json.dumps(user, cls=UserEncoder)
print(userJSON2)

'''Third way. Define a variable which uses the encode method on the custom class object. 
Pass in the user variable and print the output.'''
userJSON3 = UserEncoder().encode(user)
print(userJSON3)

# Decode custom object from JSON format back to Python. 2 ways to do this shown below.

# First way. Use the loads method, then print the output. Print the type to see that it is in fact a dict.
user2 = json.loads(userJSON)
print(user2)
print(type(user2))

# Second way. Define a function which calls upon the custom class object.
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

'''Define variable which decodes the custom object from JSON format back to a Python dictionary. 
Set the object_hook argument equal to the previously defined function. Print the type and the user's name and age.'''
user3 = json.loads(userJSON3, object_hook=decode_user)
print(type(user3))
print(user3.name)
print(user3.age)