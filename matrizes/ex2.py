#Crie um programa que calcule a soma de todos os elementos de uma matriz 2x2. A matriz pode ser qualquer valor escolhido por você.

matriz = [
    [2, 4],
    [6, 8]
]

soma = 0

for linha in matriz:
    for elemento in linha:
        soma += elemento
        
print("A soma dos elementos da matriz é: ", soma)