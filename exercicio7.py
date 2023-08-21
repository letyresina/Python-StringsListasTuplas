'''
    Exercício 7:
    Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
    a) o maior número da lista
    b) o menor número da lista
    c) a média dos números contidos na lista
'''

numeros = [] 

for i in range(10):
    num = int(input("Informe um número inteiro qualquer: "))
    numeros.append(num)

mediaAritmetica = sum(numeros) / 10

print(f"O maior número da lista é de {max(numeros)}")
print(f"O maior número da lista é de {min(numeros)}")
print(f"A média aritmética é {mediaAritmetica}")