def validar_nota():
    nota = float(input())
    while nota < 0.0 or nota > 10.0:
        print("nota invalida")
        nota = float(input())
    return nota

comando = 0

while comando != 2:
    nota1 = validar_nota()
    nota2 = validar_nota()
    print("media = %.2f" % ((nota1+nota2) / 2))
    print("novo calculo (1-sim 2-nao)")
    comando = int(input())
    while comando < 1 or comando > 2:
        print("novo calculo (1-sim 2-nao)")
        comando = int(input())
