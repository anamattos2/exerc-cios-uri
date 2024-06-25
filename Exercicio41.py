quantidade = int(input())
lista = []
for i in range (0,quantidade):
    nome_pokemon = input()
    lista.append(nome_pokemon)

lista_nova = list(set(lista))
quantidade = len(lista_nova)
print(f"Falta(m) {151-quantidade} pomekon(s).")