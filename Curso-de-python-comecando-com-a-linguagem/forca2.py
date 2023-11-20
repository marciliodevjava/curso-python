import random

def jogar():
    bem_vindo()

    list = selecionar_palavras()

    index1 = random.randrange(0, len(list))
    palavra_secreta = list[index1]
    letras_acertadas = calcula_palavra(palavra_secreta)
    tentativa = len(palavra_secreta)
    print("A palavra tem {} caractere ".format(len(palavra_secreta)))

    enforcou = False
    acertou = False
    erros = 0

    # Enquanto não enforcou e não acertou
    while not enforcou and not acertou:
        chute = pede_chute()

        if chute in palavra_secreta:
            marcar_chute(chute, palavra_secreta, letras_acertadas)
        else:
            erros = erros + 1

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        imprime_informacoes(letras_acertadas, erros)
        desenha_forca(erros)

    if acertou:
        imprime_mensagem_ganhador()

    else:
        imprime_mensagem_perdedor(palavra_secreta)

def calcula_palavra(palavra_secreta):
    lista = []
    for palavra in palavra_secreta:
        lista.append("_")
    return lista

def selecionar_palavras():
    arquivo = open("palavras.txt", "r")
    list = []
    for linha in arquivo:
        linha = linha.strip()
        list.append(linha)

    arquivo.close()
    return list

def  pede_chute():
    print("jogando.....")
    chute = input(str("Digite uma letra "))
    return chute.strip()

def marcar_chute(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute.upper() == letra.upper():
            letras_acertadas[index] = letra
        index = index + 1

def imprime_informacoes(letras_acertadas, erros):
    print("Quantidade de ERROS: {}".format(erros))
    print(letras_acertadas)

def imprime_mensagem_ganhador():
    print("Parabéns você Ganhou!!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_perdedor(palavra_secreta):
    print("Infelismente não foi dessa vez!!!")
    print("A palavra era {}".format(palavra_secreta))
    print("     _______________       ")
    print("    /               \      ")
    print("   /                 \     ")
    print("/\/                   \/\  ")
    print("\ |   XXXX     XXXX   | /  ")
    print(" \|   XXXX     XXXX   |/   ")
    print("  |   XXX       XXX   |    ")
    print("  |                   |    ")
    print("  \__      XXX      __/    ")
    print("    |\     XXX     /|      ")
    print("    | |           | |      ")
    print("    | I I I I I I I |      ")
    print("    |  I I I I I I  |      ")
    print("    \_             _/      ")
    print("      \_         _/        ")
    print("        \_______/          ")

def bem_vindo():
    print("******************************************")
    print("        Bem vindo ao jogo da Forca        ")
    print("******************************************")

def fim_jogo():
    print("******************************************")
    print("                   FIM                    ")
    print("******************************************")

# Star da aplicação
if (__name__ == "__main__"):
    jogar()
    fim_jogo()
