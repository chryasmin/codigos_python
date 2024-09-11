numeros = []

for i in range(8):
        numero = float(input(f"Número {i + 1}: "))
        numeros.append(numero)

negativos = 0
soma_positivos = 0

for numero in numeros:
        if numero < 0:
            negativos += 1
        elif numero > 0:
            soma_positivos += numero

print(f"Números negativos: {negativos}")
print(f"Soma dos números positivos: {soma_positivos}")