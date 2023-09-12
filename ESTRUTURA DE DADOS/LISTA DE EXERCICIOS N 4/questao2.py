nums=[3,9,5,2,4,6]
p=int(input('Digite 1 para ordem crescente ou 2 para ordem decrescente: '))
if p == 1:
    for i in range(len(nums)):
        nummaior=i
        for x in range(i+1, len(nums)):
            if nums[x] < nums[nummaior]:
                nummaior=x
    nums[i], nums[nummaior] = nums[nummaior], nums[i]
    print(nums)
elif p == 2:
    for i in range(len(nums)):
        nummaior = i
        for x in range(i + 1, len(nums)):
            if nums[x] > nums[nummaior]:
                nummaior = x
        nums[i], nums[nummaior] = nums[nummaior], nums[i]
    print(nums)