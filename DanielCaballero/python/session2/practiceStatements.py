import math

def is_odd_or_even(number):
    if number % 2 == 0:
        print("The number %d is even" % (number))

    else:
        print("The number %d is odd" % (number))


is_odd_or_even(5)
is_odd_or_even(4)


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


def area_of_circle(r):
    if (r > 10):
        return math.pi * r ** 2
    else:
        return "The value of radio = %d is invalid" % (r)


print(area_of_circle(12))
print(area_of_circle(3))


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


def extract_url(text):
    ext = "http://"
    url = text[text.find(ext):]
    print(url)

extract_url("we23e http://www.facebook.com/ ")