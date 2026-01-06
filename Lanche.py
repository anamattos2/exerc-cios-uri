codigo, quantidade = map(int,input().split())
if codigo == 1:
    print("Total: R$ {:.2f}".format(4*quantidade))
elif codigo == 2:
    print("Total: R$ {:.2f}".format(4.5*quantidade))
elif codigo == 3:
    print("Total: R$ {:.2f}".format(5*quantidade))
elif codigo == 4:
    print("Total: R$ {:.2f}".format(2*quantidade))
elif codigo == 5:
    print("Total: R$ {:.2f}".format(1.5*quantidade))