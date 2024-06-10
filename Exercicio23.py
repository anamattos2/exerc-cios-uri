salario = float(input())

if 0 <= salario <= 2000:
    print("Isento")
elif 2000 < salario <= 3000:
    saldo = salario-2000
    imposto = saldo*0.08
    print(f"R$ {imposto:.2f}")
elif 3000 < salario <= 4500:
    imposto1 = 1000*0.08
    imposto2 = (salario-3000)*0.18
    print(f"R$ {(imposto1+imposto2):.2f}")
elif salario > 4500:
    imposto1 = 1000*0.08
    imposto2 = 1500*0.18
    imposto3 = (salario-4500)*0.28
    print(f"R$ {(imposto1+imposto2+imposto3):.2f}")