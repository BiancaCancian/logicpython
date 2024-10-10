def ordenar_e_contar_palavras():
    entrada = input("Digite algumas palavras separadas por espaço: ")
    palavras = entrada.split()

    palavras.sort()
    print("Palavras ordenadas:", palavras)

    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    print("Contagem de palavras:")
    for palavra, quantidade in contagem.items():
        print(f"{palavra}: {quantidade}")

ordenar_e_contar_palavras()
