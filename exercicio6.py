'''
    Exercício 6:
    Escreva uma função que remova todos os espaços em branco de uma string e retorne a string 
    resultante.
'''


def removeEspacos(string):
    final = string.replace(" ", "")
    return final

print(removeEspacos(" bom dia! teste "))