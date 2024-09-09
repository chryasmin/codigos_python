'''
Essa estrutura de repetição é o mais comum em qualuqer outra liguagem de programação

for (contador = 1; contador <=5; contador++){

}
'''

#1 exemplo
for contador in range(1,6):
    print(contador)

print("----------------------------------"*4)
#2 exemplo
for contador in range(1,11,2): #3 parâmetro irá aumentar o incremento que estão sendo exibidos 
    print(contador)

print("----------------------------------"*4)
#3 exemplo - numeros do maior para o menor
for contador in range(10,1,-1): 
    print(contador,end=" ") #o comando end, informa como o phyton irá mostrar o final de uma exibição, por padrão irá da enter(\n)      