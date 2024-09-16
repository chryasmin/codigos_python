soma_positivos = 0 #inicializando a variável 
quantidade_negativos = 0
i = 0
    
while i < 10:
    valor = int(input(f"Digite o {i+1}º valor inteiro: "))
    if valor > 0:
        soma_positivos += valor
    elif valor < 0:
        quantidade_negativos += 1

    i += 1  #sempre ir aumentando até 10

print(f"Soma dos números positivos: {soma_positivos}")
print(f"Quantidade de valores negativos: {quantidade_negativos}")