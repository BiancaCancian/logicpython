#programa que multiplique duas matrizes 2x2 fornecidas pelo usuário e exiba o resultado da multiplicação. Use a fórmula da multiplicação de matrizes.


print("Digite os valores da primeira matriz 2x2:")
A = [[int(input(f"Digite A[{i}][{j}]: ")) for j in range(2)] for i in range(2)]

print("Digite os valores da segunda matriz 2x2:")
B = [[int(input(f"Digite B[{i}][{j}]: ")) for j in range(2)] for i in range(2)]

resultado = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        resultado[i][j] = A[i][0] * B[0][j] + A[i][1] * B[1][j]

print("O resultado da multiplicação das matrizes é:")
for linha in resultado:
    print(linha)
