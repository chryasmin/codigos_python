valor = int(input("Informe um valor numérico:"))

if valor >= 50:
    print(f"O número {valor} é maior ou igual a 50\n")
# elif é a junção de else if
elif valor >=30 and valor < 50:
    print(f"O número {valor} está entre 30 e 50\n")
else:
    print(f"O número {valor} é menor que 30\n")