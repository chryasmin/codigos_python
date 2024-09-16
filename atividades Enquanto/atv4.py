while True:
    nome = input("Digite seu nome(nome e sobrenome): ")
    if len(nome) >=15: #retorna o número total 
        print("NOME ACEITO, PROSSIGA!")
        break #forma de encerrar o while

    else:
        print("O nome deverá ter mais de 15 letras, por favor, tente novamente.")

