import math
import re

'''
Create 1 script to determine if a number is odd or even 
(use single line statement if applies)
'''
def is_odd_or_even(number):
    if number % 2 == 0:
        print("The number %d is even" % (number))

    else:
        print("The number %d is odd" % (number))


is_odd_or_even(5)
is_odd_or_even(4)

'''
According a list of values between a Min and Max range,
identify if the number is prime or not. 
'''
def is_prime(min, max):
    if (max < min):
        print("please enter valid values")
    else:
        for num in range(min, max + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    print("The number %d is prime" % (num))
            else:
                print("The number %d is not prime" % (num))


is_prime(2, 10)

'''
Write a function area_of_circle(r) which returns 
the area of a circle of radius r 
only if the radius value is greater of 10.
'''
def area_of_circle(r):
    if (r > 10):
        return math.pi * r ** 2
    else:
        return "The value of radio = %d is invalid" % (r)


print(area_of_circle(12))
print(area_of_circle(3))

'''
Write a function sum_to(n) that returns 
the sum of all integer numbers up to and including only 
until any value lower than 35. 
So sum_to(10)wouldbe1+2+3...+10which would return the value 55, 
but if n=40 only until sum to 35 need to be returned.  
'''
def sum_to(number):
    sum = 0
    if (number < 35):
        for i in range(1, number + 1):
            sum += i
        else:
            return sum
    else:
        for i in range(1, 36):
            sum += i
        else:
            return sum


print(sum_to(5))
print(sum_to(45))

'''
Write a function days_in_month which takes the name of a month, 
and returns the number of days in the month. Ignore leap years:
		days_in_month("February") == 28 				    
		days_in_month("December") == 31
If the function is given invalid arguments, it should return None. 
'''
def days_in_month(month):
    if month == "February":
        return 28
    elif month in ("April", "June", "September", "November"):
        return 30
    elif month in ("January", "March", "May", "July", "August", "October", "December"):
        return 31
    else:
        return ("None")


print(days_in_month("February"))
print(days_in_month("June"))
print(days_in_month("May"))
print(days_in_month("234423"))

'''
Suppose any line of text can contain 
at most one url that starts with “http://” 
and ends at the next space in the line. 
Write a fragment of code to extract 
and print the full url if it is present. 
'''
def extract_url(text):
    print (re.search("(?P<url>https?://[^\s]+)", text).group("url"))
    
extract_url("we23e http://www.facebook.com/ qdsewd")
