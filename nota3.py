import random

bem_vindo = "     Bem vindo ao jogo de nota!     "
fim_execucao = "             Fim do Jogo               "
asterisco = "******************************************"

print(asterisco)
print(bem_vindo)
print(asterisco)

numero_secreto = random.randint(0, 50)

nome = input("Digite o seu nome: \n")
idade = int(input("Digite a sua idade: \n"))
tentativas = int(input("Quantas tentativas? \n"))
print("Qual nível de dificuldade")
dificuldade = int(input("(1) - Fácil (2) - Médio (3) - Difícil \n"))

numero_facil_inicial = 0
numero_facil_final = 10
numero_medio_final = 25
numero_difil_final = 50

inicial = numero_facil_inicial
final = 10

pontos = tentativas

if dificuldade == 1:
    numero_secreto = random.randint(numero_facil_inicial, numero_facil_final)
    final = numero_facil_final
elif dificuldade == 2:
    numero_secreto = random.randint(numero_facil_inicial, numero_medio_final)
    final = numero_medio_final
elif dificuldade == 3:
    numero_secreto = random.randint(numero_facil_inicial, numero_difil_final)
    final = numero_difil_final
else:
    numero_secreto = random.randint(numero_facil_inicial, numero_facil_final)
    final = numero_facil_final

for rodada in range(1, tentativas + 1):

    # String interpolation
    print("Tentativa nº:{} de {}".format(rodada, tentativas))
    numero = int(input("Digite o seu número entre {} a {}: ".format(inicial, final)))

    if numero <= 0:
        print("Você deve digita um número maior que 0")
        pontos = pontos - 1
        continue
    else:
        if numero >= 50:
            print("Você deve digita um número menor que 50")
            pontos = pontos - 1
            continue

    acertou = numero_secreto == numero
    maior = numero > numero_secreto
    menor = numero < numero_secreto
    print("Você digitou: {}".format(numero))
    if acertou:
        print(f"Tenho uma boa noticia {nome}.")
        print("Você Acertou!!!")
        print("Você é muito inteligente e só tem", idade, "anos!", sep=" ")
        print("Você fez {} Pontos de {} Pontos".format(pontos, tentativas))
        break
    else:
        if maior:
            print(asterisco)
            print("Infelizmente você errou", nome + ".", sep=" ")
            print("É um número inferior a esse numero:", numero, sep=" ")
            print("Tente novamente.")
            pontos = pontos - 1
            print(asterisco)
        elif menor:
            print(asterisco)
            print("Infelizmente você errou", nome + ".", sep=" ")
            print("É um número superior a esse numero:", numero, sep=" ")
            print("Tente novamente.")
            pontos = pontos - 1
            print(asterisco)

print(asterisco)
print(fim_execucao)
print(asterisco)
