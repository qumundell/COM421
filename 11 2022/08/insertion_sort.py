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


list = [13,	82,	88,	46,	34,	28,	96, 78, 34,	79,	37,	55,	63,	82,	24,	49,	79,	58, 1]
sort(list)
print(list)