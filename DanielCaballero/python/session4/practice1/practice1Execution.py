from DanielCaballero.python.session4.practice1.ageCalculator import calculate_age_in_minutes, calculate_age_in_hours, \
    calculate_age_in_days
from DanielCaballero.python.session4.practice1.messages import print_message

'''
Create a script importing both modules and performing de action :
Ask to the user the amount of users
For all users define the name and the age for each one, save this data as a dictionary
After all users are defined, need to :
print the age in minutes, hours and days
The expected message according the age define
'''


global dict_users
dict_users = {}

# Creates a dictionary
def build_dictionary():
    users_quantity = int(input("Number of users: "))
    for i in range(users_quantity):
        user_name = input(f"Insert user {i + 1} name: ")
        user_age = int(input(f"Insert user {i + 1} age: "))
        dict_users[user_name] = user_age


# Prints the dictionary
def print_dictionary():
    global dict_users
    for key in dict_users:
        print(f"User {key}, age {dict_users[key]}:")
        print("Age in minutes =", calculate_age_in_minutes(dict_users[key]))
        print("Age in hours =", calculate_age_in_hours(dict_users[key]))
        print("Age in days =", calculate_age_in_days(dict_users[key]))
        print_message(dict_users[key])
        print()

build_dictionary()
print_dictionary()
