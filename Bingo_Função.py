import random

def gerar_bingo():
    # Gerar cartela
    cartela = [[' ' for i in range(5)] for j in range(5)]

    # Gerar números aleatórios
    numeros = list(range(10, 99))
    random.shuffle(numeros)

    # Colocar valores na tabela
    for i in range(5):
        for j in range(5):
            # Valor do meio
            if i == j == 2:
                cartela[i][j] = ''
            # Valores não repetidos
            else:
                cartela[i][j] = numeros.pop()

    return cartela

print("  B   I   N   G   O")
for linha in gerar_bingo():
    print(linha)