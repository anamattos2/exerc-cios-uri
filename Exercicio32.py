casos_teste = int(input())
#sheldon, raj = input().split()

for i in range (1,(casos_teste+1)):
    sheldon, raj = input().split()
    
    if sheldon == "tesoura" and raj == "papel":
        resultado = "Bazinga!"
    elif sheldon == "papel" and raj == "tesoura":
        resultado = "Raj trapaceou!"
    ##
    elif sheldon == "papel" and raj == "pedra":
        resultado = "Bazinga!"
    elif sheldon == "pedra" and raj == "papel":
        resultado = "Raj trapaceou!"
    ##
    elif sheldon == "pedra" and raj == "lagarto":
        resultado = "Bazinga!"
    elif sheldon == "lagarto" and raj == "pedra":
        resultado = "Raj trapaceou!"
    ##
    elif sheldon == "lagarto" and raj == "Spock":
        resultado = "Bazinga!"
    elif sheldon == "Spock" and raj == "lagarto":
        resultado = "Raj trapaceou!"
    ##
    elif sheldon == "Spock" and raj == "tesoura":
        resultado = "Bazinga!"
    elif sheldon == "tesoura" and raj == "Spock":
        resultado = "Raj trapaceou!"
    ##
    elif sheldon == "tesoura" and raj == "lagarto":
        resultado = "Bazinga!"
    elif sheldon == "lagarto" and raj == "tesoura":
        resultado = "Raj trapaceou!"
    ##
    elif sheldon == "lagarto" and raj == "papel":
        resultado = "Bazinga!"
    elif sheldon == "papel" and raj == "lagarto":
        resultado = "Raj trapaceou!"
    ##
    elif sheldon == "papel" and raj == "Spock":
        resultado = "Bazinga!"
    elif sheldon == "Spock" and raj == "papel":
        resultado = "Raj trapaceou!"
    ##
    elif sheldon == "Spock" and raj == "pedra":
        resultado = "Bazinga!"
    elif sheldon == "pedra" and raj == "Spock":
        resultado = "Raj trapaceou!"
    ##
    elif sheldon == "pedra" and raj == "tesoura":
        resultado = "Bazinga!"
    elif sheldon == "tesoura" and raj == "pedra":
        resultado = "Raj trapaceou!"
    else:
        resultado = "De novo!"

    print(f"Caso #{i}: {resultado}")