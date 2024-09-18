#2.	Fazer um algoritmo que preencha uma lista com 10 elementos inteiros e verifique a 
#existência de elementos iguais a 10, mostrando as posições(índices) em que apareceram

valores = []
    
for i in range(10):
    valor = int(input(f"Digite o {i+1}º valor: "))
    valores.append(valor)
    
indices_dez = []
    
for i in range(len(valores)): #len:"gera" e "limita" a sequência de números de 0 até os 10 elementos #não pecisava do len
    if valores[i] == 10:
        indices_dez.append(i)
    
if indices_dez:
    print(f"Os valores 10 foram encontrados nos índices: {indices_dez}")

else:
    print("Não há valores 10 na lista.")
