
import sys
import os

erro = 0

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]


def vitoria():
    global tabuleiro
    if tabuleiro[0][0] == "u" and tabuleiro[0][1] == "v" and tabuleiro[0][2] == "a" and tabuleiro[1][0] == "s" and tabuleiro[1][1] == "u" and tabuleiro[1][2] == "s" and tabuleiro[2][0] == "a" and tabuleiro[2][1] == "v" and tabuleiro[2][2] == "e":
        print("VOCÊ VENCEEUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")





def jogo():
    print("Bem vindo ao Palavra Cruzada!")
    for i in range(9):

        exibir_tabuleiro()

        jogada()

        vitoria()

        

def exibir_tabuleiro():
    global tabuleiro

    print("Horinzontal")
    print("1 - Fruta Roxa ")
    print("2 - Sistema de Saúde Do Brasil ")
    print("3 - Animal que Voa ")
    print("\n")

    print("    ┌───┬───┬───┐")
    print(f"1 - │ {tabuleiro[0][0]} │ {tabuleiro[0][1]} │ {tabuleiro[0][2]} │")
    print("    ├───┼───┼───┤")
    print(f"2 - │ {tabuleiro[1][0]} │ {tabuleiro[1][1]} │ {tabuleiro[1][2]} │")
    print("    ├───┼───┼───┤")
    print(f"3 - │ {tabuleiro[2][0]} │ {tabuleiro[2][1]} │ {tabuleiro[2][2]} │")
    print("    └───┴───┴───┘")

def jogada():
    global tabuleiro
    escolha = input("Escolha uma palavra : ").lower()

    if escolha not in ["uva", "sus", "ave"]:
        os.system('cls')
        print("A palavra está errada, tente novamente! \n")
    
    elif escolha == "uva":
        tabuleiro[0][0] = "u"
        tabuleiro[0][1] = "v"
        tabuleiro[0][2] = "a"
        
        os.system('cls')

    elif escolha == "sus":
        tabuleiro[1][0] = "s"
        tabuleiro[1][1] = "u"
        tabuleiro[1][2] = "s"
        os.system('cls')

    elif escolha == "ave":
        tabuleiro[2][0] = "a"
        tabuleiro[2][1] = "v"
        tabuleiro[2][2] = "e"
        os.system('cls')
 
        


jogo()
