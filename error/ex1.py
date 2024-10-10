def divisao():
    try:
        num1 = float(input("Digite o numerador: "))
        num2 = float(input("Digite o denominador: "))
        resultado = num1 / num2
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero. Tente novamente.")
    else:
        print(f"O resultado da divisão é: {resultado}")

divisao()
