def jogar():
    print("******************************************")
    print("        Bem vindo ao jogo da Forca        ")
    print("******************************************")

    palavra_secreta = "banana"
    tentativa = len(palavra_secreta)
    palavra = ""

    print("A palavra tem {} caractere ".format(len(palavra_secreta)))

    enforcou = False
    acertou = False

    #Enquanto não enforcou e não acertou
    while not enforcou and not acertou:
        print("jogando.....")
        chute = input(str("Digite uma letra "))
        if palavra_secreta.__contains__(chute):
            for letra in palavra_secreta:
                if chute == letra:
                    if len(palavra) > 1:
                        palavra = palavra + letra
                    print(chute)
                    palavra = palavra + "_"
                else:
                    if len(palavra) > 1:
                        palavra = palavra + letra
                    print("_")
                    palavra = palavra + "_"

    print("Fim do jogo")

#Star da aplicação
if (__name__ == "__main__"):
    jogar()
