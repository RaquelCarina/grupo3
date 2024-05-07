import sys

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

J1 = 0
J2 = 0


def verifica_vencedor():
    if all(tabuleiro[i][j] != " " for i in range(3) for j in range(3)):
        print("EMPATE!!")
        sys.exit()

    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] and tabuleiro[0][0] != " ":
        print("VOCÊ VENCEU!")
        sys.exit()

    elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] and tabuleiro[1][0] != " ":
        print("VOCÊ VENCEU!")
        sys.exit()

    elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] and tabuleiro[2][0] != " ":
        print("VOCÊ VENCEU!")
        sys.exit()

    elif tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] and tabuleiro[0][0] != " ":
        print("VOCÊ VENCEU!")
        sys.exit()

    elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] and tabuleiro[0][1] != " ":
        print("VOCÊ VENCEU!")
        sys.exit()

    elif tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] and tabuleiro[0][2] != " ":
        print("VOCÊ VENCEU!")
        sys.exit()

    elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != " ":
        print("VOCÊ VENCEU!")
        sys.exit()

    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != " ":
        print("VOCÊ VENCEU!")
        sys.exit()

    else:
        return False

def jogo_x():
    for i in range(9):
        exibir_tabuleiro()

        jogada_x()

        exibir_tabuleiro()

        if verifica_vencedor():
            return

        jogada_o()

        if verifica_vencedor():
            return

def jogo_o():
    for i in range(9):
        exibir_tabuleiro()

        jogada_o()

        exibir_tabuleiro()

        if verifica_vencedor():
            return

        jogada_x()
        
        if verifica_vencedor():
            return

def exibir_tabuleiro():
    global tabuleiro
    print("┌───┬───┬───┐")
    print(f"│ {tabuleiro[0][0]} │ {tabuleiro[0][1]} │ {tabuleiro[0][2]} │")
    print("├───┼───┼───┤")
    print(f"│ {tabuleiro[1][0]} │ {tabuleiro[1][1]} │ {tabuleiro[1][2]} │")
    print("├───┼───┼───┤")
    print(f"│ {tabuleiro[2][0]} │ {tabuleiro[2][1]} │ {tabuleiro[2][2]} │")
    print("└───┴───┴───┘")

def jogada_x():
    global tabuleiro
    linha = int(input("Vez de X!, digite a linha: "))
    coluna = int(input("Agora, digite a coluna: "))

    if tabuleiro[linha][coluna] != " ":
        print("O espaço esta preenchido")
    else:
        tabuleiro[linha][coluna] = "X"

def jogada_o():
    global tabuleiro
    linha = int(input("Vez de O!, digite a linha: "))
    coluna = int(input("Agora, digite a coluna: "))

    if tabuleiro[linha][coluna] != " ":
        print("O espaço esta preenchido")
    else:
        tabuleiro[linha][coluna] = "O"

def definir_jogador(x):
    global J1, J2

    if x == "X":
        J1 = "X"
        J2 = "O"
    elif x == "O":
        J1 = "O"
        J2 = "X"
    else:
        print("Você não digitou um caracter válido!")
        sys.exit()

print("Bem vindo ao jogo da velha!")
escolha = input("Escolha 'X' ou 'O': ").upper()
definir_jogador(escolha)

print("Jogador 1:", J1)
print("Jogador 2:", J2)

if J1 == "X":
    jogo_x()
elif J1 == "O":
    jogo_o()
