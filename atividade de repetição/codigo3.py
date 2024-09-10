#número 6

somar_pesos = 0
soma_idades = 0

for contador in range(5):
    peso = float(input(f"Informe seu peso {contador+1}: "))
    idade = int(input(f"Informe sua idade {contador+1}: "))

    somar_pesos = somar_pesos + peso
    soma_idades = soma_idades + idade

print (f"A média de peso do time é {somar_pesos/5}")
print (f"A média da idade do time é {soma_idades/5}")