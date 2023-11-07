import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho_senha = random.randint(10, 16)  # Gera um tamanho de senha aleatório entre 10 e 16
senha_gerada = gerar_senha(tamanho_senha)

print(f'Senha gerada: {senha_gerada}')