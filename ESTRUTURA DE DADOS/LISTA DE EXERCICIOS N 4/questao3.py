nums=[3,9,5,2,4,6,13,7,1]
for i in range(len(nums)):
    nummaior=i
    for x in range(i+1, len(nums)):
        if nums[x] < nums[nummaior]:
            nummaior=x
    nums[i], nums[nummaior] = nums[nummaior], nums[i]
print(f'O elemento máximo é {nums[-1]} e o elemento minimo e {nums[0]}.')