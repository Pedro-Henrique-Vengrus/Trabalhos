def buscaLinearContando(vetor, valor):
    comparacoes = 0

    for i in range(len(vetor)):
        comparacoes += 1
        if vetor[i] == valor:
            return i, comparacoes
        elif vetor[i] > valor:
            return None
    return None, comparacoes

def buscaBinariaContando(vetor, valor):
    inicio = 0
    fim = len(vetor) - 1
    comparacoes = 0

    while inicio <= fim:
        comparacoes += 1
        meio = (inicio + fim) // 2
        if vetor[meio] == valor:
            return meio, comparacoes
        elif vetor[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return None, comparacoes

vetor1 = list(range(1, 11))
vetor2 = list(range(1, 101))
vetor3 = list(range(1, 1001))


# ---------- BUSCA LINEAR ---------- 
print("Vetor de 10 elementos busca linear:")
teste, comparacoes = buscaLinearContando(vetor1, 1) # Esperado 1
print(f"Inicio = {comparacoes} comparacoes")
teste, comparacoes = buscaLinearContando(vetor1, 5) # Esperado 5
print(f"Meio = {comparacoes} comparacoes")
teste, comparacoes = buscaLinearContando(vetor1, 10) # Esperado 10
print(f"Fim = {comparacoes} comparacoes")
teste, comparacoes = buscaLinearContando(vetor1, 11) # Esperado 10
print(f"Ausente = {comparacoes} comparacoes\n")

print("Vetor de 100 elementos busca linear:")
teste, comparacoes = buscaLinearContando(vetor2, 1) # Esperado 1
print(f"Inicio = {comparacoes} comparacoes")
teste, comparacoes = buscaLinearContando(vetor2, 50) # Esperado 50
print(f"Meio = {comparacoes} comparacoes")
teste, comparacoes = buscaLinearContando(vetor2, 100) # Esperado 100
print(f"Fim = {comparacoes} comparacoes")
teste, comparacoes = buscaLinearContando(vetor2, 101) # Esperado 100
print(f"Ausente = {comparacoes} comparacoes\n")

print("Vetor de 1000 elementos busca linear:")
teste, comparacoes = buscaLinearContando(vetor3, 1) # Esperado 1
print(f"Inicio = {comparacoes} comparacoes")
teste, comparacoes = buscaLinearContando(vetor3, 500) # Esperado 500
print(f"Meio = {comparacoes} comparacoes")
teste, comparacoes = buscaLinearContando(vetor3, 1000) # Esperado 1000
print(f"Fim = {comparacoes} comparacoes")
teste, comparacoes = buscaLinearContando(vetor3, 1001) # Esperado 1000
print(f"Ausente = {comparacoes} comparacoes\n")

# ---------- BUSCA BINARIA ---------- 
print("Vetor de 10 elementos busca binaria:")
teste, comparacoes = buscaBinariaContando(vetor1, 1) # Esperado 3
print(f"Inicio = {comparacoes} comparacoes")
teste, comparacoes = buscaBinariaContando(vetor1, 5) # Esperado 1
print(f"Meio = {comparacoes} comparacoes")
teste, comparacoes = buscaBinariaContando(vetor1, 10) # Esperado 4
print(f"Fim = {comparacoes} comparacoes")
teste, comparacoes = buscaBinariaContando(vetor1, 11) # Esperado 4
print(f"Ausente = {comparacoes} comparacoes\n")

print("Vetor de 100 elementos busca binaria:")
teste, comparacoes = buscaBinariaContando(vetor2, 1) # Esperado 6
print(f"Inicio = {comparacoes} comparacoes")
teste, comparacoes = buscaBinariaContando(vetor2, 50) # Esperado 1
print(f"Meio = {comparacoes} comparacoes")
teste, comparacoes = buscaBinariaContando(vetor2, 100) # Esperado 7
print(f"Fim = {comparacoes} comparacoes")
teste, comparacoes = buscaBinariaContando(vetor2, 101) # Esperado 7
print(f"Ausente = {comparacoes} comparacoes\n")

print("Vetor de 1000 elementos busca binaria:")
teste, comparacoes = buscaBinariaContando(vetor3, 1) # Esperado 9
print(f"Inicio = {comparacoes} comparacoes")
teste, comparacoes = buscaBinariaContando(vetor3, 500) # Esperado 1
print(f"Meio = {comparacoes} comparacoes")
teste, comparacoes = buscaBinariaContando(vetor3, 1000) # Esperado 10
print(f"Fim = {comparacoes} comparacoes")
teste, comparacoes = buscaBinariaContando(vetor3, 1001) # Esperado 10
print(f"Ausente = {comparacoes} comparacoes")







    


