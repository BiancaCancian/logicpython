#criar um sistema que alerte se uma pessoa tem "bafo de dragão". Peça a ela quantos dentes escovou hoje. Se o número for menor que 2, 
# exiba "Cuidado! Bafo de dragão detectado!". Caso contrário, diga "Sem risco de bafo de dragão!".

dentes_escovados = int(input("Quantos dentes tu escovou? "))

if dentes_escovados < 2:
    print("Cuidado com o bafão!!")
else:
    print("Tudo ok pcr.")
    
    