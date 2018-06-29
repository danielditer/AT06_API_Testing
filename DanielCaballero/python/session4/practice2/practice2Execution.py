from DanielCaballero.python.session4.practice2.circleArea import circle_area
from DanielCaballero.python.session4.practice2.circlePerimeter import circle_perimeter


# Create a script to ask to the user of the radio and print both results.

def print_execution():
    radius = float(input("Insert radius: "))
    print("area: ", circle_area(radius))
    print("perimeter: ", circle_perimeter(radius))


print_execution()
