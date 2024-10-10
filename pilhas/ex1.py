#Você está cozinhando panquecas e quer empilhá-las. Crie um programa que empilhe 5 panquecas e depois exiba as panquecas na ordem em que serão comidas (desempilhadas).

pilhas_panquecas = []

for i in range(1,7):
    pilhas_panquecas.append(f"Panqueca {i}")
    print(f"Empilhando: Panqueca {i}")
    
print("\nHora de comer panquequitas!")

while pilhas_panquecas:
    print(f"Comendo: {pilhas_panquecas.pop()}")