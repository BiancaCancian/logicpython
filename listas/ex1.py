def gerenciar_frutas():
    frutas = ["maçã", "banana", "laranja"]
    print("Lista de frutas:", frutas)

    nova_fruta = input("Digite uma nova fruta para adicionar: ")
    frutas.append(nova_fruta)
    print("Lista de frutas após adição:", frutas)

    fruta_remover = input("Digite uma fruta para remover: ")
    if fruta_remover in frutas:
        frutas.remove(fruta_remover)
        print("Lista de frutas após remoção:", frutas)
    else:
        print(f"A fruta '{fruta_remover}' não está na lista.")

gerenciar_frutas()
