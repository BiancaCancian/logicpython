#pilha de gatos curiosos. Toda vez que um novo gato curioso aparece, ele pula para o topo da pilha. 

pilha_gatos = []

gatos = ["Gato 1", "Gato 2" , "Gato 3"]
for gato in gatos:
    pilha_gatos.append(gato)
    print(f"{gato} pulou para o topo da pilha!")
    
print("\nLiberando os gatos curiosos...")

# Desempilhando
while pilha_gatos:
    print(f"{pilha_gatos.pop()} saiu da pilha!") 