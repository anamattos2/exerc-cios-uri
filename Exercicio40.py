while True:
    try:
        senha = input()
    except EOFError:
        break
    tamanho = len(senha)
    
    if (senha.lower() != senha) and (("0" in senha) or ("1" in senha) or ("2" in senha) or ("3" in senha) or ("4" in senha) or ("5" in senha) or ("6" in senha) or ("7" in senha) or ("8" in senha) or ("9" in senha)):
        if (6 <= tamanho <=32) and senha.isalnum():
            print("Senha valida.")    
        else:
            print("Senha invalida.")
    else:
        print("Senha invalida.")
