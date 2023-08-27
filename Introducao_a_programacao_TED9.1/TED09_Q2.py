VET = []
repetidos = []
for i in range(10):
    dignum = input('Digite um número: ')
    VET.append(dignum)
for i in range(len(VET)):
    for x in range(i + 1, len(VET)):
        if VET[i] == VET[x]:
            posicaoi = i
            posicaox = x
            repetidos.append((posicaoi, posicaox))
if len(repetidos) == 0:
    print('Não houve números repetidos.')
else:
    print(f'Foram digitados {len(repetidos)} números repetidos.')
    print('Os números repetidos foram:')
    for pos in repetidos:
        print(f'{VET[pos[0]]} nas posições {pos[0]} e {pos[1]}')