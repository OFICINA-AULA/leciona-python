
idade = int(input("Digite a sua idade: "))

for i in range(1):
    if idade <110:
        print("Você é um(a) idoso(a)")
    elif idade < 63:
        print("Você é um(a) adulto")
    elif idade < 18:
        print("Você é um(a) adolescente")
    elif idade < 13:
        print("Você é uma criança")

        

match idade:
    case i if i < 13:
        print("Você é uma criança")
    case i if 13 <= i < 18:
        print("Você é um(a) adolescente")
    case i if 18 <= i < 63:
        print("Você é um(a) adulto(a)")
    case i if 63 <= i < 110:
        print("Você é um(a) idoso(a)")
    case _:
        print("Idade fora do intervalo esperado")

