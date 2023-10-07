import forca
import adivinhacao

def escolhe_jogo():
    print("******************************************")
    print("**********  Escolha o seu jogo  **********")
    print("******************************************")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Digite o número do jogo: "))

    if (jogo == 1):
        print("Jogo da Forca Selecionado")
        forca.jogar()
    elif (jogo == 2):
        print("Jogo da Adivinhação selecionado")
        adivinhacao.jogar()

escolhe_jogo()