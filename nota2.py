import random

bem_vindo = "     Bem vindo ao jogo de nota!     "
fim_execucao = "             Fim do Jogo               "
asterisco = "******************************************"

print(asterisco)
print(bem_vindo)
print(asterisco)

numero_secreto = random.randint(0, 50)

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
tentativas = int(input("Quantas tentativas? "))

for rodada in range(1, tentativas + 1):
    # String interpolation
    print("Tentativa nº:{} de {}".format(rodada, tentativas))
    numero = int(input("Digite o seu número entre 0 a 50: "))

    if (numero <= 0):
        print("Você deve digita um número maior que 0")
        continue
    else:
        if (numero >= 50):
            print("Você deve digita um número menor que 50")
            continue

    acertou = numero_secreto == numero
    maior = numero > numero_secreto
    menor = numero < numero_secreto
    print(f"Você digitou: {numero}")
    if (acertou):
        print(f"Tenho uma boa noticia {nome}.")
        print("Você Acertou!!!")
        print("Você é muito inteligente e só tem", idade, "anos!", sep=" ")
        break
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
