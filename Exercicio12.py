valor = int(input())
cedulas100 = valor//100
cedulas50 = (valor%100)//50
celulas20 = ((valor%100)%50)//20
celulas10 = (((valor%100)%50)%20)//10
cedulas5 = ((((valor%100)%50)%20)%10)//5
cedulas2 = (((((valor%100)%50)%20)%10)%5)//2
cedulas1 = (((((valor%100)%50)%20)%10)%5)%2

print(f"{valor}")
print(f"{cedulas100} nota(s) de R$ 100,00")
print(f"{cedulas50} nota(s) de R$ 50,00")
print(f"{celulas20} nota(s) de R$ 20,00")
print(f"{celulas10} nota(s) de R$ 10,00")
print(f"{cedulas5} nota(s) de R$ 5,00")
print(f"{cedulas2} nota(s) de R$ 2,00")
print(f"{cedulas1} nota(s) de R$ 1,00")