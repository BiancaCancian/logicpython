def numeros_extremos():
    numeros = []
    for i in range(5):
        numero = float(input(f"Digite o {i + 1}º número: "))
        numeros.append(numero)

    maior = max(numeros)
    menor = min(numeros)

    print(f"O maior número é {maior} na posição {numeros.index(maior)}.")
    print(f"O menor número é {menor} na posição {numeros.index(menor)}.")

numeros_extremos()
