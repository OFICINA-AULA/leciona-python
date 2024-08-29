"""
Escreva um programa que peça ao usuário para digitar uma palavra e, em seguida, 
imprima essa palavra ao contrário.
"""

# Solução proposta:
palavra = input('Digite uma palavra: ')
palavra_invertida = palavra[::-1]

print(palavra_invertida)
#-----------------------------------------------------------------------------------------
# Minha solução v1
palavra = input('Digite um palavra (v1): ')
inversa = palavra[::-1]
print(f'Palavra normal: {palavra} palavra inversa: {inversa}')
#-----------------------------------------------------------------------------------------
# Minha solução v2
palavra = list(input('Digite um palavra (v2): '))
inversa = str(palavra.reverse())
print(f'Palavra normal: {palavra} palavra inversa: {inversa}')
#-----------------------------------------------------------------------------------------
# Minha solução v3
palavra = input('Digite um palavra (v3): ')
for letra in palavra[::-1]:
    inversa +=letra   
print(f'Palavra normal: {palavra} palavra inversa: {inversa}')
