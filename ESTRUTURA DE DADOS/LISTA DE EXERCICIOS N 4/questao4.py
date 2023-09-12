nums=[]
while True:
    a=(input('Digite o numero para adicionar na lista, caso nao queria continuar digite PARAR: '))
    if a.upper()=='PARAR':
        break
    try:
        teste=float(a)
        nums.append(teste)
    except ValueError:
        print('Entrada inválida.')
for i in range(len(nums)):
    num0=i
    for x in range(i+1, len(nums)):
        if nums[x] < nums[num0]:
            num0=x
    nums[i], nums[num0] = nums[num0], nums[i]
print(f'O segundo menor numero da lista e {nums[1]}.')
print(f'A lista de numeros foi: {nums}')