idade = int(input())
anos = idade//365
meses = (idade%365)//30
dias = ((idade%365)%30)

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")