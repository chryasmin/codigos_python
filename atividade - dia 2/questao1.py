def encontrar_intersecao(lista1, lista2):
    intersecao = list(set(lista1) & set(lista2))
    return sorted(intersecao)

def main():
    lista1 = input("Digite os números da primeira lista (separados por espaço): ").split()
    lista1 = [int(num) for num in lista1]  # Convertendo para inteiros

    lista2 = input("Digite os números da segunda lista (separados por espaço): ").split()
    lista2 = [int(num) for num in lista2]  # Convertendo para inteiros
    
    resultado = encontrar_intersecao(lista1, lista2)
    print("Números comuns em ordem crescente:", resultado)
