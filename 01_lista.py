# Listas em Python funciona como vetore/matrizes [tipo excel linhas e colunas - bi ou mutidirecional]
# É dinâmica: não possuem tamanhos fixos [simplesmente as criamos e vamos adicionando elementos];
# Não tipada: Aceita quelquer tipo de dado, sem a necessidade de informar qual o tipo de dado que será armazenado
# É representada por: [] 

listamista = [1,'a','c',3,0,5,'c',['python','programação'],[1,2,3,4,5]]

  
print(listamista[8][0])
print(listamista[1],[1])
print(listamista[1],[1],[4])

# CRIANDO E DEFININDO UMA LISTA  

# É possível criar uma lista vazia;
dados = []
# Ou já definila com valores:
dados = [1,2,3,4,5]
# Ou ainda definila com valores de tipos diferentes;
dados = [1,'a',1.99,'Brasil',True]  
# o metodo list() transformará a string em uma lista de letras;
dados2 = list('Python do básico ao avançado')
# criará uma lista de números que irá de 1 á 10
numeros = list(range(11)) 

# É POSSÍVEL CRIR UMA LISTA CONTENDO OUTRAS LISTAS | OBSERVE QUE DENTRO DA LISTA PRINCIPAL TEMOS DUAS OUTRAS LISTAS
listamista = [1,'a','c',3,0,5,'c'],['python','programação'],[1,2,3,4,5]
# ADICIONANDO ELEMENTOS NUMA LISTA
#------------------------------------------------------------------------------------------------------------------------------
    # Metodo .append
letras = ['a','c','d']
print(letras)

letras.append('e')
print(letras)
    # OBS.: O METODO append PERMITE A INCLUSÃO DE UM ITEM POR VEZ, ALEM DISSO append ADICIONA O ITEM PARA O FINAL DA LISTA
#------------------------------------------------------------------------------------------------------------------------------    
    # Metodo .insert espera 2 argumentos: index e um valor
letras.insert(1,10)
print(letras)
    # OBS.: O METODO .insert SÓ É POSSÍVEL A INCLUSÃO DE UM ÚNICO ELEMENTO POR VEZ
#------------------------------------------------------------------------------------------------------------------------------  

# .extend | RECEBE UM ITERÁVEL E ADICIONA A LISTA
#------------------------------------------------------------------------------------------------------------------------------
# EXEMPLO 1

letras.extend('fgh')

print(letras)
#------------------------------------------------------------------------------------------------------------------------------
# EXEMPLO 2

letras.extend(['i','j','k'])

print(letras)

  
#------------------------------------------------------------------------------------------------------------------------------
### REMOVENDO ELEMENTOS DE UMA LISTA

#pop | REMOVE UM ELEMENTO ATRAVÉS DE SEU INDICE

#EMOVERA A LETRA 'a' QUE SE ENCONTRA NO INDICE 0

letras.pop(0)

print(letras)

letras.pop() # SE NENHUM PARAMETRO FOR PASSADO REMOVERÁ O ÚLTIMO ELEMENTO DA LISTA

  

#.remove

letras.remove('f') # REMOVE UM ELEMENTO PELO VALOR DESCRITIVO E NÃO PELO INDICE

print(letras)

  

#.clear | REMOVE TODOS OS ELEMENTOS DE UMA LISTA

### letras.clear()

### print(f'A LISTA FOI APAGADA: {letras}')

  
  

### PESQUISANDO UM ELEMENTO E RETORNANDO SEU INDICE NA LISTA

#ndice ESPERE 3 ARGUMENTOS: VALOR A SER PESQUISADO [OBRIGATÓRIO] E O RANGE: INICIO E FIM DO RANGE DE PESQUISA [OPCIONAIS]

print(letras)

#NFORMANDO APENAS O VALOR OBRIGATÓRIO A PESQUISA SERÁ FEITA DO INCIO AO FIM DA LISTA

print(letras.index('j'))

#NFORMANDO APENAS OS ARGUMENTOS VALOR E INICIO A PESQUISA SERÁ FEITA A PARTIR DO INDICE INFORMADO PARA O FIM DA LISTA

print(letras.index('C',2))

#NFORMANDO TODOS OS PARAMETROS, A PESQUISA SERÁ FEITA DENTRO DO RANGE INFORMADO

print(letras.index('e',2,5))

#BS.: CASO O VALOR INFORMADO NÃO SEJA ENCONTRADO DENTRO DO RANGE, SERÁ RETORNADO O ERRO: Valor pesquisado não está na lista

  
  
  

### RECUPERANDO VALORES DE UMA LISTA

### Através de um laço de repetição

### for i in dados:

###     print(i)

###     # Recuperando um valor expecifico através de seu index [posição] lembre-se que a posição de uma lista inicia se em 0!

# print(f'{dados[3]}: Está na posição 3 da lista')

  

### CHECANDO SE UM VALOR EXITE NA LISTA [Lembre-se o Python trabalha com case sensitive, ou seja faz direrença de maiúscula e minúscula]

#### valPesquisa = 'Brasil'

#### if valPesquisa in dados:

####     print(f'{valPesquisa}: existe na lista')

### else:

####     print(f'{valPesquisa}: não existe na lista')

#### ORDENANDO LISTA

#### OBS.: uma lista não será classificada se contiver mais de um tipo de dados, ela precisa ser de um tipo de dado apenas;

  

### numeros = [3,6,4,6,33,2,11,3,1,44,67,9] # Essa lista pode ser classificada;

#### letras = ['d','g','s','h','a'] # Essa lista pode ser classificada;

#### mista = ['g','s','h',1,2,'a'] # Essa lista não pode ser classificada, pois o tipo de dado é misto [string e inteiro];

  

#### print('--------IMPRIME NA ORDEM QUE FOI CRIADA----------------')

#### print(numeros)

#### print('--------CLASSIFICA E IMPRIME-------------')

#### numeros.sort()

#### print(numeros)

#### print('--------CLASSIFICA EM ORDEM REVERSA E IMPRIME-------------')

#### numeros.sort(reverse=True)

#### print(numeros)

  

#### ATENÇÃO! UMA LISTA NÃO PODE SER ORDENADA DURANTE UM EVENTO, OU SEJA, É PRECISO ORDENA-LA ANTES DE USAR, VEJA:

### O CÓDIGO A SEGUIR IRÁ APRESENTAR UM ERRO, POIS ESTOU TENTANDO IMPRIMIR AO MESMO TEMPO QUE CLASSIFICO.

#### print(f'TENTANDO IMPRIMIR: (numeros.sort()')  

#### ESTE EXEMPLO NÃO GERA ERRO: PRIMEIRO CLASSIFIQUEI A LISTA E DEPOIS PRINTEI SEU VALOR

#### numeros.sort()

#### print(f'TENTANDO IMPRIMIR: {numeros}')

  

#### PESQUISA E CONTA QUANTAS VEZES UM ELEMENTO É ENCONTRADO DENTRO DE UMA LISTA

#### valPesquisa = 6

#### print(f'{valPesquisa} Foin encontrado: {numeros.count(6)}')

  

#### É POSSÍVEL FAZER OPERAÇÕES COM LISTAS

#### CONCATENAR LISTAS

#### print(dados)

#### print(numeros)

#### print(f'Listas concatenadas: {dados+numeros}')

#### OPERAÇÕES MATEMÁTICAS COM LISTAS

#### lista1=[2,5,32,14,10]

#### lista2=[5,2,4,6]

#### resultado = sum(lista1+lista2)

#### print(resultado)