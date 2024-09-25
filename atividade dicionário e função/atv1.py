def mostrar_catalogo(catalogo):
    if not catalogo:
        print("O catálogo está vazio.")
    else:
        print("\nCatálogo de Livros:")
        for titulo, autor in catalogo.items():
            print(f"- {titulo} por {autor}")
    print(f"Total de livros cadastrados: {len(catalogo)}\n")

def main():
    catalogo = {}

    while True:
        print("Menu:")
        print("1. Adicionar novo livro")
        print("2. Remover um livro")
        print("3. Exibir catálogo completo")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor: ")
            catalogo[titulo] = autor
            print(f"Livro '{titulo}' adicionado com sucesso")

        elif opcao == '2':
            titulo = input("Digite o título do livro que deseja remover: ")
            if titulo in catalogo:
                del catalogo[titulo]
                print(f"Livro '{titulo}' removido com sucesso")
            else:
                print(f"Livro '{titulo}' não foi encontrado no catálogo")

        elif opcao == '3':
            mostrar_catalogo(catalogo)

        elif opcao == '4':
            print("Saindo do programa")
            break

        else:
            print("Opção inválida, tente novamente mais tarde")