soma = 0 #inicializando uma variável
total_pares = 0

for contador in range(50,71):
    if contador % 2 == 0:
        soma = soma + contador #soma +=contador
        total_pares = total_pares + 1 #total_pares +=1

print(f"A soma de todos os pares é {soma} e a média é {soma / total_pares}") 