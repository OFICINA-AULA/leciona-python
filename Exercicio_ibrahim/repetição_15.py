numero = int(input("Digite um numero: "))
eh_primo = True
for i in range(2,numero):
    if numero % i == 0:
        eh_primo = False
    break
print(f"O número {numero} é primo." if eh_primo else f"esse número não é primo.")    

