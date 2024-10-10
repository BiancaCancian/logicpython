def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivo = arr[len(arr) // 2]

    menores = [x for x in arr if x < pivo]
    iguais = [x for x in arr if x == pivo]
    maiores = [x for x in arr if x > pivo]

    return quicksort(menores) + iguais + quicksort(maiores)

numeros = [10, 7, 8, 9, 1, 5]
print("Lista ordenada:", quicksort(numeros))
