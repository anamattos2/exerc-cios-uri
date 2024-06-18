entrada = int(input())

if entrada%2 == 0: 
    for i in range(0,12):
        entrada = entrada+1
        if entrada%2 != 0:
            print(f"{entrada}")
else:
    print(f"{entrada}")
    for i in range(0,11):
        entrada = entrada+1
        if entrada%2 != 0:
            print(f"{entrada}")