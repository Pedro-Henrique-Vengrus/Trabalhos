import random

MAX_COL = 8
MAX_LIN = 8

campo = [["" for _ in range(MAX_LIN)] for _ in range(MAX_COL)]
bombas = [["" for _ in range(MAX_LIN)] for _ in range(MAX_COL)]
resultado = ""
linha = 0
coluna = 0

def inicializa_campo():
    for l in range(MAX_LIN):
        for c in range(MAX_COL):
            campo[c][l] = "-"
            if random.randint(0, 4) == 0:
                bombas[c][l] = "x"
            else:
                bombas[c][l] = ""

def imprimir_borda(ativo):
    print("   ", end="")
    for c in range(MAX_COL):
        print(f"{c+1:2}", end=" ")
    print()
    for l in range(MAX_LIN):
        print(f"{l+1:2}", end=" ")
        for c in range(MAX_COL):
            if ativo:
                print(f"[{campo[c][l]}]", end="")
            else:
                print(f" {campo[c][l]} ", end="")
        print()

def jogar():
    global linha, coluna
    imprimir_borda(True)
    while True:
        try:
            linha = int(input("linha: ")) - 1
            if 0 <= linha < MAX_LIN:
                break
        except:
            pass
        print("linha inválida")
    while True:
        try:
            coluna = int(input("coluna: ")) - 1
            if 0 <= coluna < MAX_COL:
                break
        except:
            pass
        print("coluna inválida")

def valida_estado():
    for l in range(MAX_LIN):
        for c in range(MAX_COL):
            if campo[c][l] == "-" and bombas[c][l] == "":
                return "Jogando"
    return "Ganhou"

inicializa_campo()
resultado = "Jogando"

while resultado == "Jogando":
    jogar()
    if bombas[coluna][linha] == "x":
        campo[coluna][linha] = "x"
        resultado = "Perdeu, acertou uma mina"
    else:
        campo[coluna][linha] = "v"
        resultado = valida_estado()
    imprimir_borda(True)

print(resultado)
