"""
Escreva um programa que peça ao usuário para digitar dois números e, em seguida,
imprima o produto desses números.
"""
# Solução proposta:
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
multi = lambda x,y: x * y
res = multi(num1, num2)
#-----------------------------------------------------------------------------------
# Minha solução:
numeros = input('Digite 2 números separados por virgula [num1,num2]: ').split(',')
num1,num2 = int(numeros[0]),int(numeros[1])
mult = lambda x,y:x*y
print(mult(num1,num2))