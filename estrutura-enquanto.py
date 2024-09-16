contador = 1 #inicializando a variável

while contador <=5:
    print (contador)
    contador = contador + 1 #é o mesmo que contador += 1]



    print("="*40)

    #2º forma de utlizar while - loop condicional normal

    valor = 0 #inicializando a variável
    while valor >=0:
        valor = int(input("Inform um valor(digite um valor negativo para terminar): "))

        print(f"Você digitou {valor}")

print("="*40)

#3º forma de utlizar while - como se fosse faça..enquanto
while True:
    senha = input("Informe a senha: ")
    if senha == "123":
        print("Parabéns, senha correta")
        break #forma de encerrar o while
    else:
        print("Senha incorreta, tente de novo")
