#Crie um programa que empilhe 4 missões e as conclua na ordem inversa.

pilha_missoes = []

missoes = ["Salvar a cidade", "Resgatar o gato", "Derrotar o vilão", "Ajudar o amigo"]
for missao in missoes:
    pilha_missoes.append(missao)
    print(f"Nova missão: {missao}")

print("\nHora de concluir as missões...")

while pilha_missoes:
    print(f"Missão concluída: {pilha_missoes.pop()}")
