salario = float(input("Informe um valor numérico:"))

if salario < 600.00:
    novo_salario = salario * 1.30
    print(f"Seu salário agora é: R${novo_salario:.2f}\n")
else:
    print(f"Sem direito ao aumento")

