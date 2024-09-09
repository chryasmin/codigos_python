salario = float(input("Digite o valor do salário: "))
financiamento = float(input("Digite o valor do financiamento pretendido: "))

if financiamento <=5 * salario:
    print(f"Financiamento Concedido")
    print(f"Obrigado por nos Consultar\n")

else:
    print(f"Financiamento Negado")
    print(f"Obrigado por nos Consultar\n")