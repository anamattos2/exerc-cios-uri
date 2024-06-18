while True:
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    if x == y:
        break
    elif x > y:
        print(f"Decrescente")
    elif x < y:
        print(f"Crescente")
       
        