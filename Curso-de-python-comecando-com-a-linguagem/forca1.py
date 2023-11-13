
def jogar():
    print("******************************************")
    print("        Bem vindo ao jogo da Forca        ")
    print("******************************************")

    palavra_secreta = "banana"
    letras_acertadas = calculaPalavra(palavra_secreta)
    tentativa = len(palavra_secreta)
    palavra = ""

    print("A palavra tem {} caractere ".format(len(palavra_secreta)))

    enforcou = False
    acertou = False
    erros = 0

    # Enquanto não enforcou e não acertou
    while not enforcou and not acertou:
        print("jogando.....")
        chute = input(str("Digite uma letra "))
        chute = chute.strip()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute.upper() == letra.upper():
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erros = erros + 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print("Quantidade de ERROS: {}".format(erros))
        print(letras_acertadas)

def calculaPalavra(palavra_secreta):
    lista = []
    for palavra in palavra_secreta:
        lista.append("_")
    return lista

# Star da aplicação
if (__name__ == "__main__"):
    jogar()
    print("******************************************")
    print("                   FIM                    ")
    print("******************************************")
