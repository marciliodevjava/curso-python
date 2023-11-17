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

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print("Quantidade de ERROS: {}".format(erros))
        print(letras_acertadas)

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

def pede_chute():
    print("jogando.....")
    chute = input(str("Digite uma letra "))
    return chute.strip()

def marcar_chute(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute.upper() == letra.upper():
            letras_acertadas[index] = letra
        index = index + 1

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
