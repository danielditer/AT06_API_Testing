def function1():
    array = []
    elements = int(input("Insert how many elements you want:"))
    for i in range(0, elements):
        array.append(int(input("Enter next number :")))
    return array


def function2(array):
    print(array)

function2(function1())