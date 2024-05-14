import os

tabuleiro = [
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " "],
]

def vitoria():
    global tabuleiro
    if tabuleiro[0][0] == "u" and tabuleiro[0][1] == "v" and tabuleiro[0][2] == "a":
        print("Parabéns! Você completou a palavra 'uva'!")
    if tabuleiro[0][3] == "s" and tabuleiro[0][4] == "u" and tabuleiro[0][5] == "s":
        print("Parabéns! Você completou a palavra 'sus'!")
    if tabuleiro[1][0] == "a" and tabuleiro[1][1] == "v" and tabuleiro[1][2] == "i" and tabuleiro[1][3] == "ã" and tabuleiro[1][4] == "o":
        print("Parabéns! Você completou a palavra 'avião'!")
    if tabuleiro[2][0] == "c" and tabuleiro[2][1] == "a" and tabuleiro[2][2] == "r" and tabuleiro[2][3] == "r" and tabuleiro[2][4] == "o":
        print("Parabéns! Você completou a palavra 'carro'!")
    if tabuleiro[3][0] == "b" and tabuleiro[3][1] == "o" and tabuleiro[3][2] == "l" and tabuleiro[3][3] == "a":
        print("Parabéns! Você completou a palavra 'bola'!")
    if tabuleiro[4][0] == "b" and tabuleiro[4][1] == "o" and tabuleiro[4][2] == "n" and tabuleiro[4][3] == "e" and tabuleiro[4][4] == "c" and tabuleiro[4][5] == "a":
        print("Parabéns! Você completou a palavra 'boneca'!")


def jogo():
    print("Bem vindo ao Palavra Cruzada!")
    while True:
        exibir_tabuleiro()
        jogada()

def exibir_tabuleiro():
    global tabuleiro
    print("Dicas: \n")
    print("1 - Fruta de cor roxa")
    print("2 - Sistema de saúde do Brasil")
    print("3 - Meio de transporte aéreo")
    print("4 - Veículo de quatro rodas")
    print("5 - Usado em vários esportes e tem formato esférico")
    print("6 - Brinquedo que representa um ser humano do sexo feminino")

    print("\nTabuleiro:")
    print("   1  2  3  4  5  6  7")
    for i, linha in enumerate(tabuleiro):
        print(f"{i+1} {' '.join([' ' + item + ' ' for item in linha])}")
    print()

def jogada():
    global tabuleiro
    escolha = input("Escolha uma palavra: ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    if escolha not in ["uva", "sus", "avião", "carro", "bola", "boneca", "lápis"]:
        print("Palavra incorreta! Tente novamente.\n")
        return

    if escolha == "uva":
        tabuleiro[0][0] = "u"
        tabuleiro[0][1] = "v"
        tabuleiro[0][2] = "a"
    elif escolha == "sus":
        tabuleiro[0][3] = "s"
        tabuleiro[0][4] = "u"
        tabuleiro[0][5] = "s"
    elif escolha == "avião":
        tabuleiro[1][0] = "a"
        tabuleiro[1][1] = "v"
        tabuleiro[1][2] = "i"
        tabuleiro[1][3] = "ã"
        tabuleiro[1][4] = "o"
    elif escolha == "carro":
        tabuleiro[2][0] = "c"
        tabuleiro[2][1] = "a"
        tabuleiro[2][2] = "r"
        tabuleiro[2][3] = "r"
        tabuleiro[2][4] = "o"
    elif escolha == "bola":
        tabuleiro[3][0] = "b"
        tabuleiro[3][1] = "o"
        tabuleiro[3][2] = "l"
        tabuleiro[3][3] = "a"
    elif escolha == "boneca":
        tabuleiro[4][0] = "b"
        tabuleiro[4][1] = "o"
        tabuleiro[4][2] = "n"
        tabuleiro[4][3] = "e"
        tabuleiro[4][4] = "c"
        tabuleiro[4][5] = "a"


    vitoria()

jogo()
