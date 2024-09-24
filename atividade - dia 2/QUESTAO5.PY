import random

def main():
    opcoes = ["Cara", "Coroa"]
    resultados = []

    while True:
        resultado = random.choice(opcoes)
        resultados.append(resultado)
        print(f"O resultado do lançamento é: {resultado}")

        continuar = input("Deseja lançar a moeda novamente? (s/n): ").strip().lower()
        if continuar != 's':
            break

    print("Resultados dos lançamentos:", resultados)
