nums=[3,9,5,2,4,6]
for i in range(len(nums)):
    num0=i
    for x in range(i+1, len(nums)):
        if nums[x] < nums[num0]:
            num0=x
    nums[i], nums[num0] = nums[num0], nums[i]
print(nums)