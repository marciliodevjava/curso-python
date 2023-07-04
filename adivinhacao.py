bem_vindo = "  Bem vindo ao jogo de advinhação!  "
fim_execucao = "          Fim do Jogo            "
asterisco = "************************************"

print(asterisco)
print(bem_vindo)
print(asterisco)

numero_secreto = 10
loop = True

nome = input("Digite o seu nome:")

while loop:
    numero = int(input("Digite o seu número entre 0 a 10: "))
    print("Você digitou:", numero, sep=" ")
    if (numero_secreto == numero):
        print("Tenho uma boa noticia", nome + ".", sep=" ", )
        print("Você Acertou!!!")
        loop = False
    else:
        print("Infelizmente você errou", nome + ".", sep=" ")
        print("Você Errou!!!")
        print("Tente novamente.")

print(asterisco)
print(fim_execucao)
print(asterisco)
