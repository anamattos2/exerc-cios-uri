salario_atual = float(input())

if 0 <= salario_atual <= 400:
    novo_salario = salario_atual*0.15
    print(f"Novo salario: {(novo_salario+salario_atual):.2f}")
    print(f"Reajuste ganho: {(novo_salario):.2f}")
    print(f"Em percentual: 15 %")
elif 400 < salario_atual <= 800:
    novo_salario = salario_atual*0.12
    print(f"Novo salario: {(novo_salario+salario_atual):.2f}")
    print(f"Reajuste ganho: {(novo_salario):.2f}")
    print(f"Em percentual: 12 %")
elif 800 < salario_atual <= 1200:
    novo_salario = salario_atual*0.10
    print(f"Novo salario: {(novo_salario+salario_atual):.2f}")
    print(f"Reajuste ganho: {(novo_salario):.2f}")
    print(f"Em percentual: 10 %")
elif 1200 < salario_atual <= 2000:
    novo_salario = salario_atual*0.07
    print(f"Novo salario: {(novo_salario+salario_atual):.2f}")
    print(f"Reajuste ganho: {(novo_salario):.2f}")
    print(f"Em percentual: 7 %")
elif salario_atual > 2000:
    novo_salario = salario_atual*0.04
    print(f"Novo salario: {(novo_salario+salario_atual):.2f}")
    print(f"Reajuste ganho: {(novo_salario):.2f}")
    print(f"Em percentual: 4 %")