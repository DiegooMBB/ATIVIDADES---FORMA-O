print('=====================BANCO TURMA P1 A=====================')         #QUESTÃO 5
cc=int(input('Digite o numero da sua conta: '))                             #QUESTÃO 5
SalAnt=float(input('Digite o saldo anterior: '))                            #QUESTÃO 5
ValDeb=float(input('Valor do débito: '))                                    #QUESTÃO 5
ValCred=float(input('Valor do saldo em crédito: '))                         #QUESTÃO 5
print('======================SALDO DA CONTA======================')         #QUESTÃO 5
NovoSal= SalAnt - ValDeb + ValCred                                          #QUESTÃO 5
print('O seu saldo atual é de: {:.2f}'.format(NovoSal),'reais.')            #QUESTÃO 5
if NovoSal >= 0:                                                            #QUESTÃO 5
    print('O seu saldo atual é POSITIVO.')                                  #QUESTÃO 5
else:                                                                       #QUESTÃO 5
    print('O seu saldo atual é NEGATIVO.')                                  #QUESTÃO 5
