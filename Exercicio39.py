quantidade_casos = int(input())

for i in range (0,quantidade_casos):
    lista=[]
    frase = input().split()
    for elemento in frase:
        elemento = elemento[0]
        lista.append(elemento)
    nova_palavra = "".join(lista)
    print(nova_palavra) 
