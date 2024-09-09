#numero 4

valor_inicial = int(input("Informe um valor inicial:"))
valor_final = int(input("Informe um valor final:"))

soma = 0

for cont in range(valor_inicial+1,valor_final):
    soma = soma + cont 

print(soma)
