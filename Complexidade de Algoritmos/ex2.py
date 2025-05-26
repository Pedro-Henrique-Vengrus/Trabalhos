import random

vetor1 = [random.randint(1, 100) for i in range(20)]
print(vetor1)

vetor2 = [random.randint(1, 100) for i in range(20)]
print(vetor2)

vetor3 = [random.randint(1, 100) for i in range(20)]
print(vetor3)

print(" ")
valor = int(input("Informe um valor para ser encontrado: "))
print(" ")

if valor in vetor1:
    posicao = vetor1.index(valor) 
    print(f"O valor {valor} foi encontrado no primeiro vetor e está na {posicao + 1}° posição")
else:
    print(f"O valor {valor} não foi encontrado no primeiro vetor")

if valor in vetor2:
    posicao = vetor2.index(valor)
    print(f"O valor {valor} foi encontrado no segundo vetor e está na {posicao + 1}° posição")
else:
    print(f"O valor {valor} não foi encontrado no segundo vetor")

if valor in vetor3:
    posicao = vetor3.index(valor)
    print(f"O valor {valor} foi encontrado no terceiro vetor e está na {posicao + 1}° posição")
else:
    print(f"O valor {valor} não foi encontrado no terceiro vetor")

def buscaLinear_nao_ordenado(vetor, valor):

    for i in range(len(vetor)): # Percorre o vetor até encontrar o valor
        if vetor[i] == valor:
            return i  # Retorna a posicao do valor
    return None  # Retorna None se nao encontrar

print(" ")

print("Saida =", buscaLinear_nao_ordenado(vetor1, valor) + 1)
print("Saida =", buscaLinear_nao_ordenado(vetor2, valor) + 1)
print("Saida =", buscaLinear_nao_ordenado(vetor3, valor) + 1)

