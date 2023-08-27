print('=====================ESTOQUE TURMA P1 A=====================')
EstAt=int(input('Digite a quantidade atual da mercadoria no estoque: '))
QuantMAX=int(input('Digite a quantidade máxima de mercadorias no estoque: '))
QuantMIN=int(input('Digite a quantidade mínima de mercadorias no estoque: '))
QuantMEDIA=(QuantMAX+QuantMIN)/2
print('=====================PREPARANDO VALORES=====================')
if EstAt>=QuantMEDIA:
    print('Não efetue esta compra.')
else:
    print('Pode efetuar esta compra.')