busca_linear = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

valor = int(input("Insira um valor para buscar: "))

if valor in busca_linear:
    print(f"O valor {valor} foi encontrado na lista")
else:
    print(f"Não existe o valor {valor} na lista")

posicao = busca_linear.index(valor) + 1
print(f"Ele esta na {posicao}° posição")





