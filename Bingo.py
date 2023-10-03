import random

bingo = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]

# Criar uma lista e embaralhar
numbers = list(range(10, 100))
random.shuffle(numbers)

for i in range(5):
    for j in range(5):
        bingo[i][j] = numbers.pop(0)
    bingo[2][2] = ''

print("  B   I   N   G   O")
for linha in bingo:
    print(linha)
