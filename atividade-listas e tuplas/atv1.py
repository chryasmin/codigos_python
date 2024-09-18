#1.	Elabore um algoritmo que solicite ao usuário 7 valores e insira esses valores em uma lista, após isso calcule e mostre 
#a quantidade de números ímpares que estão presentes na lista.

valores = []
    
for i in range(7):
    valor = int(input(f"Digite o {i+1}º valor: "))
    valores.append(valor) #irá inserir um novo item no final da lista
    
quantidade_impares = 0
    
  
for valor in valores:
    if valor % 2 != 0:
        quantidade_impares += 1

print(f"A quantidade de números ímpares na lista é: {quantidade_impares}")