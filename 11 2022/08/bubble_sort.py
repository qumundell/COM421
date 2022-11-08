def sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j+1]:
                tempval = nums[j]
                nums[j] = nums[j+1]
                nums[j + 1] = tempval


list = [17, 6, 23, 4, 28, 30, 54, 28, 83, 7]
sort(list)
print(list)
