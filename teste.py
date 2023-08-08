for i in range(1, 100 + 1):
    if (i == 5):
        continue
    print("Número: {:03d}".format(i))

# Float
print("Valores Float")
print("Valor R$ {:07.2f}".format(126.5))
print("Valor R$ {:07.2f}".format(51.5))
print("Valor R$ {:07.2f}".format(845.6))
print("Valor R$ {:07.2f}".format(151.51))
print()
# Inteiro
print("Valores Inteiros")
print("Valor R$ {:07d}".format(126))
print("Valor R$ {:07d}".format(51))
print("Valor R$ {:07d}".format(8456))
print("Valor R$ {:07d}".format(15151))
print()
# Data
print("Datas")
print("Data {:02d}/{:02d}/{:4d}".format(1, 2, 2023))
print("Data {:02d}/{:02d}/{:4d}".format(1, 5, 2023))
print("Data {:02d}/{:02d}/{:4d}".format(11, 12, 2023))
print("Data {:02d}/{:02d}/{:4d}".format(9, 8, 2023))
print()
# Nome
nome = 'Matheus'
print(f'Meu nome é {nome}')
print(f'Meu nome é {nome.lower()}')
print(f'Meu nome é {nome.upper()}')
