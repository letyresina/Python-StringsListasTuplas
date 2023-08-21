'''
    Exercício 4:
    Escreva um programa que receba uma frase como entrada e retorne uma lista das palavras 
    presentes na frase.
'''

def separarFrase(frase):
    palavras = frase.split()
    return palavras

frase = input("Digite uma frase: ")
print(f"A lista de palavras é de {separarFrase(frase)}")