"""
Escreva um programa que peça ao usuário para digitar um número e, em seguida, 
imprima se esse número é positivo, negativo ou zero.
"""
# Solução proposta:
def sinal(x):
    if not x:
        return 'Número é zero'
    elif (x < 0):
        return 'Número negativo'
    else:
        return 'Número positivo'


num = int(input('Digite um número: '))
print(sinal(num))
#------------------------------------------------------------------------------
# Minha solução v1:
numero = int(input('Digite um número inteiro qualquer: '))
match numero:
    case 0:
        print(f'O número: {numero} é zero.')
    case x if x <0:
        print(f'O número: {numero} é negativo.')
    case _:
        print(f'O número: {numero} é positivo.')
#------------------------------------------------------------------------------
# Minha solução v2:
def tpEntrada(num: int):
    if num %2 == 0:
        return 'positivo'
    elif num <0:
        return 'negativo'
num = int(input('Digite um número inteiro qualquer: '))
print(f'O número {num} é {tpEntrada(num)}')


        