a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

lista = [a, b, c, d, e , f]
lista_positivos = []

contador = 0
for i in lista:
    if i > 0:
        contador += 1
        lista_positivos.append(i)
        media = sum(lista_positivos)/len(lista_positivos)
print(f"{contador} valores positivos")
print(f"{media}")