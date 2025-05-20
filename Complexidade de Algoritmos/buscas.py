def buscaLinear_nao_ordenado(vetor, valor):

    for i in range(len(vetor)): # Percorre o vetor até encontrar o valor
        if vetor[i] == valor:
            return i  # Retorna a posicao do valor
    return None  # Retorna None se nao encontrar



def buscaLinear_ordenado(vetor, valor):

    for i in range(len(vetor)): # Percorre o vetor ordenado
        if vetor[i] == valor:
            return i
        elif vetor[i] > valor: # Se o vetor for maior que o valor ele encerra
            return None
    return None



def busca_binaria(vetor, valor):

    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:    # loop indicando que enquanto o inicio for menor ou igual ao fim ele vai executar as condicionais
        meio = (inicio + fim) // 2    # aqui pega o tamanho inteiro do vetor e faz uma media aritmetica para descobrir o meio

        if vetor[meio] == valor:
            return meio
        elif vetor[meio] < valor:    # Aqui os vetores sao divididos no meio, para encontrar o valor elimina uma metade do vetor
            inicio = meio + 1
        else:
            fim = meio - 1

    return None



vetor_nao_ordenado = [12, 6, 8, 7, 2, 14]
vetor_ordenado = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Saida =", buscaLinear_nao_ordenado(vetor_nao_ordenado, 8)) # Resposta esperada: 2
print("Saida =", buscaLinear_ordenado(vetor_ordenado, 7)) # Resposta esperada: 6
print("Saida =", busca_binaria(vetor_ordenado, 2)) # Resposta esperada: 1

print("Saida =", buscaLinear_nao_ordenado(vetor_nao_ordenado, 3)) # Resposta esperada: None
print("Saida =", buscaLinear_ordenado(vetor_ordenado, 11)) # Resposta esperada: None
print("Saida =", busca_binaria(vetor_ordenado, 11)) # Resposta esperada: None