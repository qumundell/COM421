def sort(nums):
    lownum = None
    lowindex = None
    for i in range(len(nums)):
        for j in range(len(nums) - 1,i, -1):
            if lownum is None:
                lownum = nums[j]
                lowindex = j
            if lownum > nums[j]:
                lownum = nums[j]
                lowindex = j

        tempval = nums[lowindex]
        nums[lowindex] = nums[i]
        nums[i] = tempval
        lownum = None



list = [17, 6, 23, 4, 28, 30, 54, 28, 83, 7]
sort(list)
print(list)