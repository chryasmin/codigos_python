import random
valores = {i: 0 for i in range(1, 7)}

for _ in range(10): #for _ in, mantêm do 1 ao 6, 10 vezes
        resultado = random.randint(1, 6) #random.randint - random sorteia o número e randint que retorna o número sorteado
        valores[resultado] += 1 

for valor, quantidade in valores.items():
        print(f"O valor {valor} foi sorteado {quantidade} vezes.")