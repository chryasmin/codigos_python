animais = ['cachorro', 'gato','ovelha']
print(type(animais)) #exibindo o tipo da variável

print(animais)

print('-'*50)

#ESTAMOS EXIBINDO TODOS OS ITENS DA LISTA 'ANIMAIS'
for elementos in animais:
    print(elementos)

#1º etapa: Atualização de dados
print('-'*50)
animais[0] = 'Coelho'
print(animais)

#2º etapa: Inserir dados na lista
print('-'*50)
#forma 1 - usando append
animais.append("Cavalo")#irá inserir um novo item n final da lista
print(animais)

#forma 2 - usando insert
animais.insert(1, "Pássaro") #o insert precisa de 2 valores, o 1º será o íncide da lisa que desejo inserir o valor. O 2º é o conteúdo que quero inserir na lista
print(animais)

#3º etapa: Excluir itens da lista
print('-'*50)

#forma 1 - usando pop()
animais.pop()#irá excluir sempre o último elemento
print(animais)

#forma 2 - usando pop() com índice
animais.pop(0) #Aqui iremos escolher qual índice da lista será excluído

#forma 3 - usando remove
animais.remove("Ovelha")#irá remover o irem pelo seu conteúdo
print(animais)



