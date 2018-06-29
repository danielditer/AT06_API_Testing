user_dict = {}

'''
Function that will create a dictionary with a list of userID and userName,
the userID should be only numbers between 1 to 100.
Username should be only lowercase (nor more than 8 digits)
'''


def create_dictionary():
    global user_dict
    flag = True
    while flag:
        print()
        response = input("Insert user? Yes: y, No: n ")
        if response.lower() == "n":
            flag = False
        elif response.lower() == "y":
            user_id = int(input("Insert user_id: "))
            user_name = input("Insert user_name: ")
            if 0 < user_id < 101 and len(user_name) < 9:
                user_dict[user_id] = user_name
            else:
                print("user_id or user_name is out of range")
                continue


'''
Function that is going to request to the user for a number (only 1 number) 
and need to return the amount of users that have their user ID starting with the number inserted 
(E.g. if user inserted 1, then could count all users with 1, 10,11,12,13..19 or 100), 
return and array with the user_ID that fulfilled this condition
'''


def number_request():
    global user_dict
    user_id_list = []
    number = int(input("Insert a number: "))
    for key in user_dict.keys():
        if str(key).startswith(str(number)):
            user_id_list.append(key)
    return user_id_list


'''
Function that is going to request to the user for a character (only 1 char) 
and need to return the amount of users that have their  userName 
starting with the character inserted (E.g. if user inserted a, 
then could count all users that start with a), 
return and array with the list of userName that fulfilled this condition
'''


def character_request():
    global user_dict
    user_name_list = []
    character = input("Insert a character: ")
    for key in user_dict:
        if user_dict[key].startswith(character):
            user_name_list.append(user_dict[key])
    return user_name_list


'''
Function to display a message considering :
UseID between 1-25 “User belong Group 1”
UseID between 26-50 “User belong Group 2”
UseID between 51-75 “User belong Group 3”
UseID between 76-100 “User belong Group 4”
'''


def print_user_group():
    global user_dict
    for key in user_dict:
        if 0 < key < 26:
            print(f"User {user_dict[key]} belongs to Group 1")
        elif 25 < key < 51:
            print(f"User {user_dict[key]} belongs to Group 2")
        elif 50 < key < 76:
            print(f"User {user_dict[key]} belongs to Group 3")
        elif 75 < key <= 100:
            print(f"User {user_dict[key]} belongs to Group 4")


create_dictionary()
print()
print(number_request())
print()
print(character_request())
print()
print_user_group()
