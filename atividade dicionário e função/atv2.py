def calcular_media(notas):
    return sum(notas) / len(notas) if notas else 0

def alunos_acima_da_media(catalogo, media):
    return {aluno: nota for aluno, nota in catalogo.items() if nota > media}

def main():
    catalogo = {}

    while True:
        nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        
        nota_valida = False
        while not nota_valida:
            nota_input = input(f"Digite a nota de {nome}: ")
            if nota_input.replace('.', '', 1).isdigit() and float(nota_input) >= 0:
                nota = float(nota_input)
                catalogo[nome] = nota
                print(f"Aluno {nome} adicionado com a nota {nota}")
                nota_valida = True
            else:
                print("Nota inválida. Por favor, insira uma nota válida")

    if catalogo:
        media = calcular_media(list(catalogo.values()))
        print(f"\nMédia da turma: {media:.2f}")

        alunos_acima = alunos_acima_da_media(catalogo, media)
        if alunos_acima:
            print("Alunos com notas acima da média:")
            for aluno, nota in alunos_acima.items():
                print(f"{aluno}: {nota:.2f}")
        else:
            print("Nenhum aluno teve nota acima da média")
    else:
        print("Nenhum aluno foi cadastrado")