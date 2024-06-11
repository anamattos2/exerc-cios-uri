texto,dia_in = input().split(" ")
hh,mm,ss = input().split(" : ")
texto,dia_fim = input().split(" ")
hh_fim,mm_fim,ss_fim = input().split(" : ")

dia_in = int(dia_in)
hh = int(hh)
mm = int(mm)
ss = int(ss)

dia_fim = int(dia_fim)
hh_fim = int(hh_fim)
mm_fim = int(mm_fim)
ss_fim = int(ss_fim)

dia_in_seg = dia_in*86400
hora_seg = (hh*60*60)
min_seg = (mm*60)
total_hora_inicial = dia_in_seg + hora_seg + min_seg + ss

dia_fim_seg = dia_fim*86400
hora_fim_seg = (hh_fim*60*60)
mm_fim_seg = (mm_fim*60)
total_hora_fim = dia_fim_seg + hora_fim_seg + mm_fim_seg + ss_fim

duracao_segundos = total_hora_fim - total_hora_inicial

if duracao_segundos > 0:
    dias = duracao_segundos//86400
    horas = (duracao_segundos%86400)//3600
    minutos = ((duracao_segundos%86400)%3600)//60
    segundos = ((duracao_segundos%86400)%3600)%60
    print(f"{dias} dia(s)")
    print(f"{horas} hora(s)")
    print(f"{minutos} minuto(s)")
    print(f"{segundos} segundo(s)")
    
elif duracao_segundos < 0:
    duracao = duracao_segundos + (24*60*60)
    dias = duracao//86400
    horas = (duracao%86400)//3600
    minutos = ((duracao%86400)%3600)//60
    segundos = ((duracao%86400)%3600)%60
    print(f"{dias} dia(s)")
    print(f"{horas} hora(s)")
    print(f"{minutos} minuto(s)")
    print(f"{segundos} segundo(s)")




