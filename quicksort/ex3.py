def quicksort(arr, nivel=0):
    
    print("  " * nivel + f"Lista: {arr}")
    
    if len(arr) <= 1:
        return arr
    
    pivo = arr[len(arr) // 2]
    print("  " * nivel + f"Pivô escolhido: {pivo}")
    
    menores = [x for x in arr if x < pivo]
    iguais = [x for x in arr if x == pivo]
    maiores = [x for x in arr if x > pivo]
    
    print("  " * nivel + f"Menores: {menores}, Iguais: {iguais}, Maiores: {maiores}")
    
    return quicksort(menores, nivel + 1) + iguais + quicksort(maiores, nivel + 1)

numeros = [33, 10, 55, 26, 7, 2, 90]
print("Ordenação passo a passo:")
print(quicksort(numeros))
