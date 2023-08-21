'''
    Exercício 11:
    Preencha duas tuplas com 5 números cada, informados pelo usuário. Concatene as duas 
    tuplas e exiba a tupla resultante.
'''

def preencherTupla():
    tupla = ()
    for i in range(5):
        num = int(input("Informe um número inteiro qualquer: "))
        tupla += (num,)  # Adiciona o número à tupla usando a concatenação de tuplas
    return tupla

tupla1 = preencherTupla()
tupla2 = preencherTupla()

tupla = tupla1 + tupla2
print(f"Tupla resultante: {tupla}")
