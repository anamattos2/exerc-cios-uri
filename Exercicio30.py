valor1 = int(input())
contador = 0
contador2 = 0
vetor = [valor1]

for contador in range(1,10):
    valores = int(input())
    vetor.append(valores)
    
print(f"{vetor}")
# vetor = [(1 if (x == 0) or (x < 0) else x) for x in vetor]

vetor_temp = []
for x in vetor:
    if (x == 0) or (x < 0):
        vetor_temp.append(1)
    else:
        vetor_temp.append(x)
vetor = vetor_temp

print(f"{vetor}")
       
for contador2 in range(0,10):
    print(f"X[{contador2}] = {vetor[contador2]}")