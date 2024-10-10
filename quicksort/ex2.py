def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivo = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivo]
    iguais = [x for x in arr if x == pivo]
    maiores = [x for x in arr if x > pivo]
    return quicksort(menores) + iguais + quicksort(maiores)

entrada = input("Digite uma lista de números separados por espaço: ")
numeros = list(map(int, entrada.split()))

print("Lista ordenada:", quicksort(numeros))
