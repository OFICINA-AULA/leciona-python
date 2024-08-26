lista = (1,2,3,4,5,6)
for lista in range(6):
    print(lista)
print('----------------------------------')    
lista = (1,2,3,4,5,6)
print(enumerate(lista))
print(type(enumerate(lista)))
print(list(enumerate(lista)))
for item in lista:
    print(lista[item-1])