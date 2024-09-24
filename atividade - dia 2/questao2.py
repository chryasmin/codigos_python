def main():
    notas = []
    
    while True:
        nota = float(input("Digite a nota do aluno (ou 0 para terminar): "))
        if nota == 0:
            break
        notas.append(nota)

    if len(notas) == 0:
        print("Nenhuma nota foi registrada.")
        return

    media = sum(notas) / len(notas)
    alunos_acima_media = sum(1 for nota in notas if nota > media)

    print(f"A média da turma é: {media:.2f}")
    print(f"Número de alunos com notas acima da média: {alunos_acima_media}")
