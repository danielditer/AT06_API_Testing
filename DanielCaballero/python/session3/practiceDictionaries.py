'''
Write a program that reads a string and returns
a table of the letters of the alphabet in alphabetical order
which occur in the string together with the number of times each letter occurs.
'''
def letter_count():
    string = input("Enter a sentence")

    string = string.lower()

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    array = {}
    for char in string:
        if char in alphabet:
            if char in array:
                array[char] = array[char] + 1
            else:
                array[char] = 1

    keys = array.keys()
    for char in sorted(keys):
        print(char, array[char])

letter_count()


global dict1
dict1 = {}

'''
Function to create the dictionary, the Function should ask for the length of the dictionary
According the length defined should ask to the user for the key and for the value.
'''
def create_dictionary():
    elements = int(input("Insert how many elements you want:"))
    for i in range(0, elements):
        key = input("Insert the key for the next element ")
        value = input("Insert the value for the next element")
        dict1[key] = value
    return dict1

#Function to print the dictionary keys
def print_dict_keys():
    print(dict1.keys())

#Function to print the dictionary values
def print_dict_values():
    print(dict1.values())

#Function to print the dictionary
def print_dictionary():
    print(dict1)

#Function to define is a key inserted by the user, exists on the dictionary.
def key_exists(key):
    if key in dict1.keys():
        print(dict1[key])
    else:
        print("The key %d doesn't exist in the dictionary" % (key))

#Function to define is a value inserted by the user, exists on the dictionary.
def value_exists(value):
    print(value in dict.values())

'''
Define a function that can return 
a dictionary where the keys are numbers between 1 and 9 (both included) 
and the values are square of keys.
'''
def square_of_keys():
    dictionary = dict()
    for i in range(1, 9):
        dictionary[i] = i ** 2
    return dictionary

create_dictionary()
print_dict_keys()
print_dict_values()
print_dictionary()
key_exists("a")
value_exists(1)
square_of_keys()
