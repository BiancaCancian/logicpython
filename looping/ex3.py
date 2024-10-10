#Simule um jogo de adivinhação onde o programa escolhe um número aleatório entre 1 e 5, e o usuário deve adivinhar. 
# O jogo continua até o usuário acertar o número.

import random

n_real = random.randint(1, 5)

while True:
    palpite = int(input("Escolha um número entre 1 e 5: "))
    
    if palpite == n_real:
        print("Bom de chute!")
        break
    else:
        print("Burro Pkrl!")