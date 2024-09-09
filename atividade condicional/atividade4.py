altura = float(input("Informe sua altura(em metros): "))
sexo = input("Informe o seu sexo(m para masculino, f para feminino): ")

if sexo == 'm':
    peso_ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é {peso_ideal:.2f}")
elif sexo == 'f':
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é {peso_ideal:.2f}")