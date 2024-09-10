horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_hora = float(input("Digite o valor por hora:R$ "))
salario = (horas_trabalhadas, valor_hora)

if horas_trabalhadas > 40:
    horas_normais = 40
    horas_extras = horas_trabalhadas - 40
    salario_base = horas_normais * valor_hora
    bonus_extras = horas_extras * valor_hora * 1.5
    
else:
    horas_normais = horas_trabalhadas
    horas_extras = 0
    salario_base = horas_normais * valor_hora
    bonus_extras = 0

salario_total = salario_base + bonus_extras

print(f"O salário total é: R${salario_total:.2f}")