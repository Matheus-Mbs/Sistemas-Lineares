import copy

mainMatriz = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

termosIndep = [0,0,0]

def CalcDeterminante(matriz):
    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]

    principal = (a * e * i) + (b * f * g) + (c * d * h)

    secundaria = (c * e * g) + (a * f * h) + (b * d * i)

    return principal - secundaria

def CalcX():
    detX = copy.deepcopy(mainMatriz)

    for i in range(3):
        detX[i][0] = termosIndep[i]

    return CalcDeterminante(detX)

def CalcY():
    detY = copy.deepcopy(mainMatriz)

    for i in range(3):
        detY[i][1] = termosIndep[i]


    return CalcDeterminante(detY)

def CalcZ():
    detZ = copy.deepcopy(mainMatriz)

    for i in range(3):
        detZ[i][2] = termosIndep[i]


    return CalcDeterminante(detZ)

def CalcMain():
    detMain = copy.deepcopy(mainMatriz)

    return CalcDeterminante(detMain)


def inputMatriz():
    for row in range(3):
        for column in range(3):
            mainMatriz[row][column] = int(input('Digite o valor da matriz seguindo sua ordem: '))

        termosIndep[row] = int(input('Digite o termo independente da equação: '))

    detMain = CalcMain()

    if detMain == 0:
        print('Erro! Determinante principal igual a zero!')
    else:
        X = CalcX() / detMain
        Y = CalcY() / detMain
        Z = CalcZ() / detMain

        solution = [X,Y,Z]

        print(solution)

def menu():
    while True:
        option = input('1- Calcular o sistema\n2- Sair\nDigite a opção: ')

        if option == '1':
            inputMatriz()
        else:
            print('Programa encerrado!')
            break

menu()