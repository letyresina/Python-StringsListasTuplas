'''
    Exercício 10:
    Preencha duas listas, uma para armazenar os nomes e outra para armazenar as idades de 
    pessoas. A entrada de dados deve ser finalizada quando o usuário informar um nome vazio.
    Na sequência informe o nome de todas as pessoas que possuem idade igual ou superior a 
    18 anos.
'''

nomes = []
idades = []

def buscarIdade(nomes, idades):
    for i in range(len(nomes)):
        if idades[i] >= 18:
            print(f"As pessoas com 18 anos ou mais são: {nomes[i]}")

while True:
    nome = input("Informe o nome da pessoa: ")
    if nome == "":
        break
    idade = int(input("Informe a idade da pessoa: "))
    nomes.append(nome)
    idades.append(idade)


buscarIdade(nomes, idades)
