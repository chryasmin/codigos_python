contagem_impares = 0

while True:
    valor = int(input("Digite um valor numérico (ou 0 para parar): "))
    if valor == 0:
     break
    elif valor % 2 != 0:  #!: quando não é divisível
        contagem_impares += 1
    
print(f"Quantidade de valores ímpares: {contagem_impares}")
