pessoa = ["Maria", "48", "Rua 10"]
print(pessoa)

#INICIANDO COM DICIONÁRIO
dados_pessoais = {
    'nome':'João',
    'Idade': 23,
    'Endereço':'Avenida 4'
} #toda vez que usar dicionário usa chaves;
#Oque vem antes dos dois pontos é chamado de chave, e depois dos dois pontos é chamado de valor;
print(dados_pessoais)


#EXIBINDO AS CHAVES UTILIZANDO O COMANDO KEYS()
print(dados_pessoais.keys())


#EXIBINDO TANTO AS CHAVES QUANTO O VALOR COM O COMANDO ITEMS()
print(dados_pessoais.items())


#EXIBINDO UM DICIONÁRIO DETALHADO
for chave, valor in dados_pessoais.items():
    print(f"{chave} : {valor}")

#REALIZANDO OPERAÇÕESMCOM DICIONÁRIO 
#ADICIONANDO DADOS AO DICIONÁRIO

#1º FORMA
dados_pessoais["Peso"] = 68
print(dados_pessoais)

#2º FORMA
dados_pessoais.update({"Profissão":"Engenheiro"})
print(dados_pessoais)

#REMOVER DADOS DO DICIONÁRIO

#1º FORMA - USANDO pop()
dados_pessoais.pop("Endereço")
print(dados_pessoais)

#2º FORMA - USANDO del()
del(dados_pessoais["nome"])
print(dados_pessoais)



