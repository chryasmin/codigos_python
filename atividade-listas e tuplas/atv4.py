#4.Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
#Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram 
#(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temperaturas = []
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    
print("Informe a temperatura média de cada mês: ")

for i in range(12):
    temperatura = float(input(f"{meses[i]}: "))
    temperaturas.append(temperatura)
    
total_temperaturas = 0

for temperatura in temperaturas:
    total_temperaturas += temperatura
    
    media_anual = total_temperaturas / len(temperaturas)
    
print(f"Média anual das temperaturas: {media_anual:.2f}°C")
print("Temperaturas acima da média: ")
    
for i in range(len(temperaturas)):
    if temperaturas[i] > media_anual:
        print(f"{meses[i]}: {temperaturas[i]:.2f}°C")
