quant_registro = int(input())
contador = 0
while contador < quant_registro:
    contador += 1
    registro_academico = input()
    senha_geral = int(registro_academico[2::])
    if registro_academico[0:2] != "RA":
        print("INVALID DATA")
    elif len(registro_academico) < 20:
        print("INVALID DATA")
    else:
        print(senha_geral)

