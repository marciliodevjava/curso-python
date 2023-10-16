import random


def jogar():
    asterisco = "******************************************"
    bem_vindo = "        Bem vindo ao jogo da Forca        "

    print(asterisco)
    print(bem_vindo)
    print(asterisco)

    secreta = {"banana", "pera", "abacate", "limao", "açai", "morango", "manga", "laranja"}
    palavra_secreta = random.choice(list(secreta))
    tentativa = len(palavra_secreta)
    palavra = ""

    enforcou = False
    acertou = False
    frase = ""
    tentativa = 1
    fim_jogo = "FIM DE JOGO"
    total = 1

    print("A palavra tem {} caractere {}".format(len(palavra_secreta), str(contadorSegredor(palavra_secreta))))
    print("\nVocê tem {} TENTATIVAS".format(6))

    # Enquanto não enforcou e não acertou
    while not enforcou and not acertou:
        print("")
        print(asterisco)
        chute = input(str("Digite uma letra: \n"))
        chute = chute.lower()
        contador = 0
        if palavra_secreta.__contains__(chute):
            for letra in palavra_secreta:
                if len(palavra) == len(palavra_secreta):
                    if palavra.__contains__(letra):
                        print(letra.upper(), end="")
                        frase = frase + letra
                        contador += len(letra)
                    elif palavra_secreta[contador].__contains__(chute):
                        print(letra.upper(), end="")
                        frase = frase + letra
                        contador += len(letra)
                    elif palavra[contador] == letra:
                        frase = frase + letra
                        print(letra.upper(), end="")
                    else:
                        print("_", end="")
                        frase = frase + "_"
                        contador += len(letra)
                if len(palavra) < len(palavra_secreta):
                    if chute == letra:
                        if len(palavra) != len(palavra_secreta):
                            print(letra.upper(), end="")
                            frase = frase + letra
                            palavra = palavra + chute
                            contador += len(letra)
                    else:
                        print("_", end="")
                        palavra = palavra + "_"
                        frase = frase + "_"
                        contador += len(letra)
            palavra = frase
            frase = ""
            print("\nVocê tem {} TENTATIVAS".format(total))
            print("Número de ERROS Nº:{}".format(tentativa - 1))
        else:
            total = str(6 - tentativa)
            print("\nVocê tem {} TENTATIVAS".format(total))
            tentativa = tentativa + 1
            print("Número de ERROS Nº:{}".format(tentativa - 1))
            while tentativa == 7:
                print(palavra)
                enforcou = True
                acertou = True
                break


        if palavra == palavra_secreta:
            acertou = True
            print(asterisco)
            print("\nPARABÉNS!!!!! \nVOCÊ GANHOU!!!!!! \n")
            print(asterisco)

    print("Palavra SECRETA era: {}".format(palavra_secreta).upper())
    print(fim_jogo)
    print(asterisco)

def contadorSegredor(palavra:str):
    tamanho = ""
    for contador in palavra:
        tamanho = tamanho + "_"

    return tamanho


# Star da aplicação
if (__name__ == "__main__"):
    jogar()
