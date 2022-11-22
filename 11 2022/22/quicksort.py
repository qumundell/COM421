def quickSort(numbers, start, end):
    pivot = end
    if start >= end:
        return
    pivot = hoares(numbers,0, len(numbers) - 1, pivot)
    quickSort(numbers, start, pivot -1)
    quickSort(numbers, pivot+1, end)

def hoares(numbers, i, j,pivot):
    while True:
        while i <= pivot and numbers[i] < numbers[pivot]:
            i += 1
        while j >= pivot and numbers[j] > numbers[pivot]:
            j -= 1
        if i>=j:
            return(pivot)
        tempVal = numbers[i]
        if pivot == i:
            pivot = j
        elif pivot == j:
            pivot = i
        numbers[i] = numbers[j]
        numbers[j] = tempVal




numbers = [22,56,1,59,38,7,15,17,33]
quickSort(numbers,0,len(numbers) - 1)
print(numbers)
