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



vetor_ordenado = [1, 3, 5, 7, 9, 11, 13]

print("Saida =", buscaLinear_ordenado(vetor_ordenado, 9)) # Resposta esperada: 4
print("Saida =", busca_binaria(vetor_ordenado, 9)) # Resposta esperada: 4