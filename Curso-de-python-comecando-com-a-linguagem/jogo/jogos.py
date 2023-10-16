import forca
import adivinhacao

def escolhe_jogo():
    asterico = "******************************************"
    print(asterico)
    print("**********  Escolha o seu jogo  **********")
    print(asterico)

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Digite o número do jogo: \n"))

    if (jogo == 1):
        print(asterico)
        print("====>   Jogo da FORCA Selecionado    <====")
        forca.jogar()
    elif (jogo == 2):
        print(asterico)
        print("===>  Jogo da ADIVINHAÇÃO selecionado <===")
        adivinhacao.jogar()

escolhe_jogo()