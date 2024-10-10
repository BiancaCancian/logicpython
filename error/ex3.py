def acesso_lista():
    lista = [10, 20, 30, 40, 50]
    try:
        indice = int(input("Digite um índice de 0 a 4 para acessar a lista: "))
        print(f"O elemento na posição {indice} é: {lista[indice]}")
    except IndexError:
        print("Erro: Índice fora do intervalo. Tente um índice de 0 a 4.")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

acesso_lista()
