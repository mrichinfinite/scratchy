# Import modules
import sys
from helper import *
from ruamel import yaml
import json
import xml.etree.ElementTree as ET

import xml.dom.minidom as MD

# Main function
if __name__ == "__main__":
    #########################################
    #              Procedure 1              #
    #########################################
    # Add print statement here
    print("DevNet")

    #########################################
    #              Procedure 2              #
    #########################################
    print('##################')
    print('###### YAML ######')
    print('##################')

    # Open the user.yaml file as read only, use the open function to open user.yaml as a stream.
    with open ('user.yaml', 'r') as stream:
        # Load the stream using safe_load. Use the safe_load function from the ruamel.yaml module to load the stream. Save the object into a variable called user_yaml.
        user_yaml = yaml.safe_load(stream)
    # Print the object type. Determine which type of an object is the user_yaml variable, using the type function. Print the result.
    print("Type of user_yaml variable:")

    print(type(user_yaml)) # Psst: it's a dictionary (class == 'dict') type of object :)

    # Iterate over the keys of the user_yaml variable and print them, using a for loop. The dictionary keys are the same as in the user.yaml file, and you can use them to access the values in the user_yaml variable.
    print('Keys in user_yaml:')
    for key in user_yaml:
        print(key)
    print('----------------------')

    # Create a new instance of class User and name the variable user. The User object has multiple attributes that have already been defined in the User class, which is located in the helper.py file (helper module). You will assign the values from the user_yaml variable into this object.
    user = User()
    # Assign values from the user_yaml to the object user. Assign the user object attributes the values from the corresponding user_yaml keys. The object attributes and the dictionary keys have the same names. You can also check the attribute names in the helper.py file.
    user.id = user_yaml['id']
    user.first_name = user_yaml['first_name']
    user.last_name = user_yaml['last_name']
    user.birth_date = user_yaml['birth_date']
    user.address = user_yaml['address']
    user.score = user_yaml['score']

    # Print the user object
    print('User object:')
    print(user)

    #########################################
    #              Procedure 3              #
    #########################################
    print('##################')
    print('###### JSON ######')
    print('##################')

    # Create JSON structure from the user object
    user_json = json.dumps(user, default = serializeUser)
    # The dumps function takes a variable and produces a JSON string. It knows how to encode dictionaries, lists, and simple values, such as strings and numbers. However, custom objects, like the user variable, might have internal, private state that makes no sense if written to a string. That's why user-defined objects require a custom serialization function; specify it as a named-argument called default. Use the provided serializeUser function from the helper module to serialize the user variable. Save the JSON structure into the user_json variable.
    
    # Print the created JSON structure
    print('Print user_json:')
    print(user_json)
    print('----------------------')

    # Create JSON structre with indents and soreted keys
    print('JSON with indents and sorted keys')
    user_json = json.dumps(user, default = serializeUser, indent=4, sort_keys=True)
    print(user_json)
    #########################################
    #              Procedure 4              #
    #########################################
    print('######################')
    print('# XML - Element Tree #')
    print('######################')

    # Parse the user.xml file. Save the ElementTree instance into a variable named tree.
    tree = ET.parse('user.xml')
    # Get the root element. Use the getroot() function of ElementTree to get the root element of the tree variable and save it into a variable named root.
    root = tree.getroot()
    # Print the tags of the XML file using a for loop to iterate through the elements in the root variable. The tag is accessible with the .tag attribute of an element.
    print('Tags in the XML:')    
    for element in root:
        print(element.tag)
    print('----------------------')

    # Print the value of id tag. The find function of the Element object takes a string as a parameter and returns the Element with the same tag name as the string. Use the find function on the root variable to find the ID element, and use the .text attribute of the Element object to get the value of the ID tag and print it.
    print('id tag value:')
    print(root.find('id').text)
    print('----------------------')

    # Find all elements with the tag address in root. Similar to the find function, which finds the first element with the specified tag, the findall function returns all the elements with the specified tag. Use the findall function of the root variable to get all elements with the tag "address", and assign the value to a variable named addresses.
    addresses = root.findall('address')
    # Print the addresses in the xml. Write a nested loop to print the tags and values of the XML elements in the addresses variable.
    print('Addresses:')
    for address in addresses:
        for i in address:
            print(i.tag + ': ' + i.text)
    print('----------------------')
    
    # Print the elements in root with their tags and values. Iterate through the root variable using the iter function and print all element tags and values.
    print('Print the structure')    
    for k in root.iter():
        print(k.tag + ': ' + k.text)
    # Parsing XML files with MiniDOM 
    print('######################')
    print('### XML - MiniDOM ####')
    print('######################')

    # Parse the user.xml file using the parse function of the MD module. Save the returned DOM object into a variable named dom.
    dom = MD.parse('user.xml')
    # Print the tags using the printTags function in the helper module to print the tags of the child nodes of the dom variable. Iterate through the child nodes of the dom variable, and pass the child nodes list of the iterator to the printTags function.
    print('Tags in the XML:')
    for node in dom.childNodes:
        printTags(node.childNodes)
    print('----------------------')    

    # Accessing element value. Use the getElementsByTagName function and pass the "id" tag as a string for the argument. Assign the returned value to the idElements variable. The variable will contain a list of NodeList objects with nodes that have the tag name "id".
    print('Accessing element value')
    idElements = dom.getElementsByTagName('id')
    print(idElements)
    # The location of the DOM Element in the memory differs each time the code is run, so your output will differ from the example.

    # To access the Element object in a NodeList object, use the item function and pass it an integer value. Because there is a single item in the idElements node list, the integer value should be 0. Save the Element object into a variable named elementId.
    elementId = idElements.item(0)
    # Print the child nodes of the elementId element using the property childNodes, which returns a list of nodes contained within elementId.
    print(elementId.childNodes)
    # Because there is a single element in the elementId node, use the firstChild property to access it and the data property to get the value of the ID tag. Save the value into a variable named idValue.
    idValue = elementId.firstChild.data
    # Print the idValue variable to verify that the obtained value is the correct one.
    print(idValue)
    print('----------------------')
    

    # Print elements from the DOM with tag name 'address'. Use the functions getElementsByTagName and printNodes to print all the child elements of the address tags. Loop over the elements and pass the child nodes to the printNodes function from the helper.py module.
    print('Addresses:')
    for node in dom.getElementsByTagName('address'):
        printNodes(node.childNodes)
    print('----------------------')

    # Print the entire structure with printNodes. In a similar way as before, write the code that prints all the nodes and their values of the dom variable. Iterate over the child nodes of the dom variable, and pass the child nodes for the iterator to the printNodes function.
    print('The structure:')
    for node in dom.childNodes:
        printNodes(node.childNodes)

    #########################################
    #              Procedure 5              #
    #########################################
    print('######################')
    print('#   Use Namespaces   #')
    print('######################')

    # Parse the user.xml file. Use the parse function of ET to parse the item.xml file. Save the ElementTree instance into a variable named itemTree.
    itemTree = ET.parse('item.xml')
    # Get the root element. Use the getroot function of ElementTree to get the root element of the itemTree variable.
    root = itemTree.getroot()
    # Define namespaces. Define the two namespaces into a dictionary named namespaces. The keys are 'a' and 'b', and the corresponding values are the a and b namespaces from the item.xml file.
    namespaces = {'a':'https://www.example.com/network', 'b':'https://www.example.com/furniture'}
    # Set table as the root element. Using the findall function, set the table element as the root element of the two namespaces. Use elementsInNSa as the variable for the 'a' namespace and elementsInNSb for the 'b' namespace. Pass the findall function the tags and the namespaces dictionary.
    elementsInNSa = root.findall('a:table', namespaces)
    elementsInNSb = root.findall('b:table', namespaces)
    # Elements in NS a. Use a double for loop to print the tags and texts of the elements in the namespace 'a'.
    print('Elements in NS a:')   
    for e in elementsInNSa:
        for i in e.iter():
            print(i.tag + ': ' + i.text)
    print('----------------------')

    # Elements in NS b. Similarly, do the same for the namespace 'b'. Use the list function; pass the first element of elementsInNSb and iterate over these elements. Print the tag and text of each element.
    print('Elements in NS b:')
    for element in list(elementsInNSb[0]):
        print(element.tag + ': ' + element.text)