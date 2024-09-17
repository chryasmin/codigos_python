#trabalhando com objetos
objetos = ('Lápis','borracha','caderno') #iniciou com esses 3 itens, morreu com esses 3 itens

print(type(objetos)) #a função type() irá exibir o tipo da variável 'objetos', nesse caso irá aparecer 'tuple'

print(objetos)
print(objetos[1]) #estamos exibindo apernas um item, que está na posição 1


#EXIBINDO TODOS OS DADOS DA TUPLA
print('-'*50)
for item in range(0,3):
    print(objetos[item])


#EXIBINDO TODOS OS DADOS SEM A FUNÇÃO RANGE
print('-'*50)

for item in objetos:
    print(item)

#TENTANDO MUDAR O CONTEÚDO DA TUPLA
print('-'*50)

objetos[0] = "Caneta"
print(objetos)