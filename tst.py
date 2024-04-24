tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

def jogo_x():
    for i in range(9):
        exibir_tabuleiro()

        jogada_x()

        exibir_tabuleiro()

        jogada_o()

        exibir_tabuleiro()

def jogo_o():
    for i in range(9):
        exibir_tabuleiro()

        jogada_o()

        exibir_tabuleiro()

        jogada_x()

        exibir_tabuleiro()

def exibir_tabuleiro():
    global tabuleiro
    print("┌───┬───┬───┐")
    print(f"│ {tabuleiro[0][0]} │ {tabuleiro[0][1]} │ {tabuleiro[0][2]} │")
    print("├───┼───┼───┤")
    print(f"│ {tabuleiro[1][0]} │ {tabuleiro[1][1]} │ {tabuleiro[1][2]} │")
    print("├───┼───┼───┤")
    print(f"│ {tabuleiro[2][0]} │ {tabuleiro[2][1]} │ {tabuleiro[2][2]} │")
    print("└───┴───┴───┘")

J1 = 0
J2 = 0

def jogada_x():
    global tabuleiro
    linha = int(input("Digite a linha: "))
    coluna = int(input("Digite a coluna: "))

    tabuleiro[linha][coluna] = "X"

def jogada_o():
    global tabuleiro
    linha = int(input("Digite a linha: "))
    coluna = int(input("Digite a coluna: "))

    tabuleiro[linha][coluna] = "O"


def definir_jogador(x):
    global J1, J2

    if x == "X":
        J1 = "X"
        J2 = "O"
    else:
        J1 = "O"
        J2 = "X"

print("Bem vindo ao jogo da velha!")
escolha = input("Escolha 'X' ou 'O': ").upper()
definir_jogador(escolha)

print("Jogador 1:", J1)
print("Jogador 2:", J2)

if J1 == "X":
    jogo_x()
else:
    jogo_o()