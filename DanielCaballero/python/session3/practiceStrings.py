'''
Write a function replace(s, old, new)
that replaces all occurrences of old with new in a string s:
'''

def replace(s, old, new):
    words = s.split(old)
    new_string = new.join(words)
    return new_string

print(replace("Mississippi", "i", "I"))
print(replace("I love spom! Spom is my favorite food.Spom, spom, yum!", "om", "am"))
print(replace("I love spom! Spom is my favorite food.Spom, spom, yum!", "o", "a"))
