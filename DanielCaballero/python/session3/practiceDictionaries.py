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


def create_dictionary():
    elements = int(input("Insert how many elements you want:"))
    for i in range(0, elements):
        key = input("Insert the key for the next element ")
        value = input("Insert the value for the next element")
        dict1[key] = value
    return dict1


def print_dict_keys():
    print(dict1.keys())


def print_dict_values():
    print(dict1.values())


def print_dictionary():
    print(dict1)


def key_exists(key):
    if key in dict1.keys():
        print(dict1[key])
    else:
        print("The key %d doesn't exist in the dictionary" % (key))


def value_exists(value):
    print([k for k, v in dict1.items() if v == value])


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
