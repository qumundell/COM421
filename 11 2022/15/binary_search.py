import math

def binary_search(list, toFind):
    lowBound = 0
    highBound = len(list) - 1
    midpoint = None
    while lowBound < highBound:
        midpoint = math.floor((lowBound + highBound)/2)
        if list[midpoint] == toFind:
            lowBound = highBound
            print(f"Your number is the square number of {midpoint + 1}")
            return True
        elif list[midpoint] < toFind:
            lowBound = midpoint + 1
            print(f"lowBound is {lowBound}")
        else:
            highBound = midpoint - 1
            print(f"highBound is {highBound}")


numbers = [i*i for i in range(1, 101)]
toFind = int(input("Which number do you want to find the root of?"))
if binary_search(numbers, toFind) is not True:
    print("Your number is not a square number")

