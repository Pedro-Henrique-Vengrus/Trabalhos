while True:
    numero = int(input("Digite um número de 1 a 10 (ou 0 para sair): "))

    if numero == 0:
        print("Saindo...")
        break
    elif 1 <= numero <= 10:
        print(f"Tabuada do {numero}:")
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
        print("-" * 10)
    else:
        print("Só pode numeros de 1 a 10!!")
