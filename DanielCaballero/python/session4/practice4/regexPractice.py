import re

'''
Add a method that is going to ask for a username :
Need to be write with lowercase letter (a-z), number (0-9), an underscore
'''
def validate_username(username):
    expression = re.compile("[a-z0-9-_]*$")
    result = str(expression.match(username))
    if result != 'None':
        print("Valid username")
    else:
        print("Invalid username ")

'''
Add a method that is going to ask for a password:
Need to be write with lowercase letter (a-z), number (0-9), 
letter (A-Z) and the length have to be between 8 and 16 characters
'''
def validate_password(password):
    expression = re.compile("[a-zA-Z0-9]{8,16}$")
    result = str(expression.match(password))
    if result != 'None':
        print("Valid password")
    else:

        print("Invalid password")

'''
Add a method that is going to ask for email
Need to have the format anything@domain.com  
(could accept also country e.g. anything@domain.com.bo)
'''
def validate_email(email):
    expression = re.compile('^[\w]+@[\w-]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,2})?$')
    result = str(expression.match(email))
    print("Valid email" if result != 'None' else "Invalid email")


validate_username("NNNNNN")
validate_username("danielditer890_")

validate_password("ewgfherjf7678668m")
validate_password("DAN78k78")

validate_email("anything@domain.com")
validate_email("anything@domain.com.bo")
validate_email("anything@domain.com.bol")
