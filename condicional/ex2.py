#pergunte ao usuário se ele está com fome. Se a resposta for "sim", exiba "Vá pegar um lanche!". Se for "não", exiba "Continue com seus estudos!".

fome = input("Are you hungry? (yes/no) ")

if fome.lower() == "yes":
    print("You need to eat now!!")
else:
    print("You need to studie now!")
    
