import random

numeros_sorteados = random.sample(range(1, 61), 6) 
print(numeros_sorteados, end="\n\n")

numeros_escolhidos = []

for i in range(6):
    valor = int(input(f"Insira o {i + 1}° numero: "))
    while valor in numeros_escolhidos:
        print("Nao pode repetir o mesmo numero!")
        valor = int(input(f"Insira o {i + 1}° numero: "))

    numeros_escolhidos.append(valor)

print(f"\nOs numeros escolhidos foram", end=" ")

for n in numeros_escolhidos[:-1]:
    print(n, end=", ")

print(numeros_escolhidos[-1])

def buscaLinear_nao_ordenado(vetor, valor):

    for i in range(len(vetor)): # Percorre o vetor até encontrar o valor
        if vetor[i] == valor:
            return i  # Retorna a posicao do valor
    return None  # Retorna None se nao encontrar

acertos_numeros = []

for n in numeros_escolhidos:
    if buscaLinear_nao_ordenado(numeros_sorteados, n) != None:
        acertos_numeros.append(n)

print("Os numeros que voce acertou foram:", end=" ")

if acertos_numeros:
    for n in acertos_numeros[:-1]:
        print(n, end=", ")
    print(acertos_numeros[-1])
else:
    print("0")

print(f"Voce acertou o total de {len(acertos_numeros)} numeros")

if len(acertos_numeros) == 6:
    print("Voce ganhou!")
else:
    print("Voce perdeu!")
