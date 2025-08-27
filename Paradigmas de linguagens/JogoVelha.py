def mostrar_tabuleiro(tabuleiro):
    valores = [str(i+1) if tabuleiro[i] == " " else tabuleiro[i] for i in range(9)]
    print(f" {valores[0]} | {valores[1]} | {valores[2]} ")
    print("---+---+---")
    print(f" {valores[3]} | {valores[4]} | {valores[5]} ")
    print("---+---+---")
    print(f" {valores[6]} | {valores[7]} | {valores[8]} ")

def verificar_vencedor(tabuleiro, simbolo):
    combinacoes_de_vitoria = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in combinacoes_de_vitoria:
        if tabuleiro[a] == simbolo and tabuleiro[b] == simbolo and tabuleiro[c] == simbolo:
            return True
    return False

tabuleiro = [" "] * 9
jogador_atual = "X"

while True:
    mostrar_tabuleiro(tabuleiro)
    escolha = input(f"Vez do jogador {jogador_atual}. Escolha de 1 a 9: ").strip().lower()
    if not escolha.isdigit():
        print("Entrada inválida.")
        continue
    posicao = int(escolha)
    if posicao < 1 or posicao > 9:
        print("Posição inválida.")
        continue
    if tabuleiro[posicao-1] != " ":
        print("Posição já ocupada.")
        continue
    tabuleiro[posicao-1] = jogador_atual
    if verificar_vencedor(tabuleiro, jogador_atual):
        mostrar_tabuleiro(tabuleiro)
        break
    if " " not in tabuleiro:
        mostrar_tabuleiro(tabuleiro)
        break
    jogador_atual = "O" if jogador_atual == "X" else "X"
