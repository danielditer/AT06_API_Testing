# Module messages

'''
Create 1 module to print 4 different messages :
You are a child, when the age is lower than 12
Your are teenager, when the age is between 13 and 17
You are young, when the age is between 18 and 29
You are adult, when the age is greater than 30
'''

# Prints a message according to age entered as input.
def print_message(age: int):
    if -1 < age <= 12:
        print("You are a child, when the age is lower than 12")
    elif 12 < age < 18:
        print("Your are teenager, when the age is between 13 and 17")
    elif 18 <= age < 30:
        print("You are young, when the age is between 18 and 29")
    elif age >= 30:
        print("You are adult, when the age is greater than 30")
