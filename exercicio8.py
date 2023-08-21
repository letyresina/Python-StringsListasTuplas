'''
    Exercício 8:
    Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
    a) a quantidade de números pares contidos na lista
    b) o somatório de todos os números ímpares contidos na lista
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

print(f"A quantidade de números pares contidos na lista é de {len(pares)}")
print(f"O somatório de numeros ímpares é de {sum(impares)}")