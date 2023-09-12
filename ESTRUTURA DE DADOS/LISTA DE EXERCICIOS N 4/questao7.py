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
        nummaior=i
        for x in range(i+1, len(nums)):
            if nums[x] < nums[nummaior]:
                nummaior=x
nums[i], nums[nummaior] = nums[nummaior], nums[i]
print(f'O terceiro maior numero da lista e {nums[-3]}.')
print(f'A lista de numeros foi: {nums}')