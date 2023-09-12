nums=[3,9,5,2,4,6]
contp=0
contimp=0
for i in range(len(nums)):
    nummaior = i
    for x in range(i + 1, len(nums)):
        if nums[x] > nums[nummaior]:
            nummaior = x
    nums[i], nums[nummaior] = nums[nummaior], nums[i]
for i in nums:
    if i%2==0:
        contp+=1
    else:
        contimp+=1
print(f'A lista em ordem decrescente foi: {nums}.')
print(f'O contador de par foi: {contp} e o contador de impar foi: {contimp}.')