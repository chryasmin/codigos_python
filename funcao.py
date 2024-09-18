#SEPARAÇÃO DO CÓDIGO PARA DEIXAR O ALGORITMO MAIS EFICIENTE, PARA QUE NÃO HAJA REPETIÇÃO DE CÓDIGO

#DEF: DEFINIR UMA FUNÇÃO
  #função com retorno 
def somar(num1, num2):
    resultado = num1 + num2

    return resultado #devolvendo um valor para quem chamoua função 

  #chamando a função
print(somar(10,5)) 

  #função sem retorno
def multiplicar(valor1, valor2):
    resultado = valor1 * valor2
    print(resultado)

  #chamando a função
multiplicar(2,6)

