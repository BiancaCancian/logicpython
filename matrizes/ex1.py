#Escreva um programa que crie uma matriz 3x3 (3 linhas e 3 colunas) e exiba seus elementos.

matriz = [
    [1,5,4],
    [2,4,6],
    [5,6,7]
]

for linha in matriz:
    for elemento in linha:
        print(elemento, end="  ")
    print()