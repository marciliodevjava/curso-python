def jogar():
    print("******************************************")
    print("        Bem vindo ao jogo da Forca        ")
    print("******************************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]
    tentativa = len(palavra_secreta)
    palavra = ""

    print("A palavra tem {} caractere ".format(len(palavra_secreta)))

    enforcou = False
    acertou = False

    # Enquanto não enforcou e não acertou
    while not enforcou and not acertou:
        print("jogando.....")
        chute = input(str("Digite uma letra "))
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_acertadas[index] = letra

            index = index + 1

        print(letras_acertadas)

# Star da aplicação
if (__name__ == "__main__"):
    jogar()
