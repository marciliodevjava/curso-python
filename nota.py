import random

bem_vindo = "     Bem vindo ao jogo de nota!     "
fim_execucao = "             Fim do Jogo               "
asterisco = "******************************************"

print(asterisco)
print(bem_vindo)
print(asterisco)

numero_secreto = random.randint(0, 50)
loop = True

nome = int(input("Digite a quantidade de aluno"))
nome = input("Digite o seu nome: ")
tentativas = 0;

while loop:
    numero = int(input("Digite o seu número entre 0 a 50: "))
    tentativas += 1
    acertou = numero_secreto == numero
    maior = numero > numero_secreto
    menor = numero < numero_secreto
    print("Você digitou:", numero, sep=" ")
    if (acertou):
        print("Tenho uma boa noticia", nome + ".", sep=" ", )
        print("Você Acertou!!!")
        print("Tetativas: ", tentativas, sep=" ")
        print("Você é muito inteligente e só tem", idade, "anos!", sep=" ")
        loop = False
    else:
        if maior:
            print(asterisco)
            print("Infelizmente você errou", nome + ".", sep=" ")
            print("É um número inferior a esse numero:", numero, sep=" ")
            print("Tente novamente.")
            print(asterisco)
        elif menor:
            print(asterisco)
            print("Infelizmente você errou", nome + ".", sep=" ")
            print("É um número superior a esse numero:", numero, sep=" ")
            print("Tente novamente.")
            print(asterisco)


print(asterisco)
print(fim_execucao)
print(asterisco)
