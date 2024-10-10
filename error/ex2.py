def entrada_inteiro():
    try:
        numero = int(input("Digite um número inteiro: "))
        print(f"O número digitado é: {numero}")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

entrada_inteiro()
