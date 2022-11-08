def sort(nums, divider=0):
    if divider == 0:
        sort(nums, divider + 1)

    elif nums[divider - 1] > nums[divider]:
        tempval = nums[divider]
        nums[divider] = nums[divider - 1]
        nums[divider - 1] = tempval
        sort(nums)

    if divider != len(nums) - 1:
        sort(nums, divider + 1)


list = [17, 6, 23, 4, 28, 30, 54, 28, 83, 7]
sort(list)
print(list)