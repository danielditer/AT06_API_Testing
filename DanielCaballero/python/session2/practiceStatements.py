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


is_prime(6, 10)


def area_of_circle(r):
    if (r > 10):
        return math.pi * r ** 2
    else:
        return "The value of %d is invalid" % (r)

print(area_of_circle(12))