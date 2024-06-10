hora_ini, min_ini, hora_fim, min_fim = input().split()
hora_ini = int(hora_ini)
min_ini = int(min_ini)
hora_fim = int(hora_fim)
min_fim = int(min_fim)
    
min_ini_total = (hora_ini*60) + min_ini
min_fim_total = (hora_fim*60) + min_fim

if min_ini_total > min_fim_total:
    min_fim_total= min_fim_total + (24*60) #pode ser min_ini_total+= (24*60)
    
duracao_min = min_fim_total - min_ini_total
du_hora = duracao_min//60
du_min = duracao_min%60
if du_hora == 0 and du_min == 0:
    print(f"O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print(f"O JOGO DUROU {du_hora} HORA(S) E {du_min} MINUTO(S)")