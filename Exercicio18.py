inicio, fim = [int(v) for v in input().split()]
if inicio >=12 or inicio == 0:
    duracao = 24 - inicio + fim
    print (f"O JOGO DUROU {duracao} HORA(S)")
else:
    duracao2 = (fim - inicio)
    print (f"O JOGO DUROU {duracao2} HORA(S)")