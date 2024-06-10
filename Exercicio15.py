codigo, quant = input().split()
codigo = int(codigo)
quant = int(quant)

if codigo == 1:
    print(f"Total: R$ {(quant*4):.2f}")
elif codigo == 2:
    print(f"Total: R$ {(quant*4.50):.2f}")
elif codigo == 3:
    print(f"Total: R$ {(quant*5):.2f}")
elif codigo == 4:
    print(f"Total: R$ {(quant*2):.2f}")
elif codigo == 5:
    print(f"Total: R$ {(quant*1.50):.2f}")