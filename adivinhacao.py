bem_vindo = "  Bem vindo ao jogo de advinhação!  "
fim_execucao = "          Fim do Jogo            "
asterisco = "************************************"

print(asterisco)
print(bem_vindo)
print(asterisco)

numero_secreto = 42

nome = input("Digite o seu nome:")
numero = int(input("Digite o seu número: "))

print("Você digitou:", numero, sep=" ")
if(numero_secreto == numero):
    print("Tenho uma boa noticia", nome + ".", sep=" ",)
    print("Você Acertou!!!")
else:
    print("Infelizmente você errou", nome + ".", sep=" ")
    print("Você Errou!!!")

print(asterisco)
print(fim_execucao)
print(asterisco)
