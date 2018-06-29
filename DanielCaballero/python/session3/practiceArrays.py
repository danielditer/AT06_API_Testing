'''
Function 1:
No arguments defined
Should ask to the user the number of elements in the list
According the value inserted ask for each value of the array and push it in a new array
Return the array
'''
def function1():
    array = []
    elements = int(input("Insert how many elements you want:"))
    for i in range(0, elements):
        array.append(int(input("Enter next number :")))
    return array

'''
Function 2
Should receive 1 argument (the array returned in method 1)
should print the array
'''
def function2(array):
    print(array)

function2(function1())