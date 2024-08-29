"""
Escreva um programa que peça ao usuário para digitar um número e, em seguida, 
imprima os números ímpares de 0 até esse número.
"""
# Solução proposta:
def num_impar(x):
    impar = []
    for i in range(x):
        if i % 2 != 0:
            impar.append(i)
        else:
            continue
    return impar

num = int(input('Digite um número: '))
impar = num_impar(num)
print(impar)
#----------------------------------------------------------------------
# Minha solução
num = int(input('Digite um número inteiro qualquer: '))
impares = [impar for impar in range(num) if impar % 2 ==1]
print(impares)