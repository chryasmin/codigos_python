percurso = float(input("Digite o percurso em quilômetros: "))
tipo_carro = int(input("Digite o tipo do carro (1, 2, 3): "))

if tipo_carro == 1:
    consumo = percurso / 8
    print(f"O consumo de gasolina para este percurso será de {consumo:.2f} litros")
elif tipo_carro == 2:
    consumo = percurso / 9
    print(f"O consumo de gasolina para este percurso será de {consumo:.2f} litros")
elif tipo_carro == 3:
    consumo = percurso / 12
    print(f"O consumo de gasolina para este percurso será de {consumo:.2f} litros")

else:
    print(f"Dados Inválidos")