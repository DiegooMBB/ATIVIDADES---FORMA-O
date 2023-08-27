print('=================QUESTÃO 2=================')
n1=float(input('Digite o valor da primeira nota: '))
n2=float(input('Digite o valor da segunda nota: '))
md=float((n1+n2)/2)
if md>=6:
    print('O aluno teve uma media %.2f e foi aprovado.'%md)
else:
    print('O aluno teve uma media %.1f e foi reprovado.'%md)
