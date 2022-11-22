import math
def mergesort(numbers):
    midpoint = math.floor(len(numbers)/2)
    list1 = [numbers[i] for i in range(midpoint)]
    if len(list1) > 1:
        list1 = mergesort(list1)
        print(list1)
    list2 = [numbers[i] for i in range(midpoint, len(numbers))]
    if len(list2) > 1:
        list2 = mergesort(list2)
        print(list2)
    mergedlist = merge(list1, list2)
    print(mergedlist)
    return mergedlist

def merge(list1, list2):
    counter1 = 0
    counter2 = 0
    sortedList = []
    while counter1 < len(list1) and counter2 < len(list2):
        if list1[counter1] < list2[counter2]:
            sortedList.append(list1[counter1])
            counter1 += 1
        elif list2[counter2] < list1[counter1]:
            sortedList.append(list2[counter2])
            counter2 += 1
        else:
            sortedList.append(list1[counter1])
            sortedList.append(list2[counter2])
            counter1 +=1
            counter2 +=1
    if counter1 < len(list1):
        for i in range(counter1, len(list1)):
            sortedList.append(list1[i])
    elif counter2 < len(list2):
        for i in range(counter2, len(list2)):
            sortedList.append(list2[i])
    return sortedList

number = [22, 56, 1, 59, 38, 7, 15, 17, 33]
number = mergesort(number)
print(number)