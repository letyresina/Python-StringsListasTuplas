'''
    Exercício 9:
    Preencha uma lista com 10 números digitados pelo usuário. A partir desta lista, gere uma lista 
    com os números pares e outra com os números ímpares. 
'''

numeros =[]
pares = []
impares = []

for i in range(10):
    num = int(input("Informe um número inteiro qualquer: "))
    numeros.append(num)

for item in numeros:
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)

print(f"\n Pares: {pares} \n Ímpares: {impares} \n")