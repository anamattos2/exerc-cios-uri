lista_frases = []
lista_maiores = []
contador = -1
while True:
    frase = input().split(" ")
    if frase == ["0"]:
        break
    
    lista_frases.append(frase)
    
#print(lista_frases)

for palavra in lista_frases:
    lista_quantidade_letras = []
    for letras in palavra:
        quantidade_letras = str(len(letras))
        lista_quantidade_letras.append(quantidade_letras)
    maior = max(palavra, key=len)
    lista_maiores.append(maior)
    print('-'.join(lista_quantidade_letras))

#print(lista_maiores)
lista_maiores.reverse()

maiorzona = max(lista_maiores, key = len)
print("")
print(f"The biggest word: {maiorzona}")