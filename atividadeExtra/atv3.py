temperaturas = []
print("Digite 7 temperaturas:")

for i in range(7):
        temperatura = float(input(f"Temperatura {i + 1}: "))
        temperaturas.append(temperatura) #append - adicionar um item ao final de uma lista

soma = 0
for temp in temperaturas: # temp - assumir o valor de cada item na lista
        soma += temp

media = soma / 7

igual_ou_acima = 0
abaixo = 0

for temp in temperaturas:
        if temp >= media:
            igual_ou_acima += 1
        else:
            abaixo += 1

print(f"Temperaturas iguais ou acima da média: {igual_ou_acima}")
print(f"Temperaturas abaixo da média: {abaixo}")