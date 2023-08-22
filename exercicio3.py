'''
    Exercício 3:
    Crie uma função que retorne a quantidade de vogais (a, e, i, o, u) existentes em uma string
'''


def quantidadeVogais(palavra):
    cont = 0
    vogais = 'aeiouAEIOU'
    for i in palavra:
        if i in vogais:
            cont += 1
    return cont
    

print(quantidadeVogais("Leticia"))