#Você foi desafiado a provar que não é um robô! Peça para o usuário responder à famosa pergunta: "Qual é a cor do céu durante o dia?".
# Se a resposta for "azul", exiba "Você não é um robô!". Caso contrário, diga "Robô detectado!".

resposta = input("Qual é a cor do céu quando está de dia? ")

#lower - tornar comparações de strings mais robustas, ignorando diferenças entre maiúsculas e minúsculas.
if resposta.lower() == "azul":
    print("Você não é um robô.")
else:
    print("Robô detectado!!!")