'''
    Exercício 5:
    Implemente uma função que retorne a quantidade de palavras existentes em uma string.
'''

def quantidadePalavras(string):
    palavras = string.split()
    return len(palavras)

print(quantidadePalavras("Socorro"))


