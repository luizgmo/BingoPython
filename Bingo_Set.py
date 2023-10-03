import random

# Gerar matriz
cartela = []

# Conjunto para acompanhar os números escolhidos
numeros_escolhidos = set()

# Gerar números aleatórios e não repetidos nas linhas e colunas
for i in range(5):
    linha = []
    for j in range(5):
        while True:
            numero = random.randint(10,99)
            if numero not in numeros_escolhidos:
                numeros_escolhidos.add(numero)
                linha.append(numero)
                break

    cartela.append(linha)

cartela[2][2] = ''

print("  B   I   N   G   O")
for linha in cartela:
    print(linha)
