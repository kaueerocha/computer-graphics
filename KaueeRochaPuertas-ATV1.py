import numpy as np
import math

# LETRA A
def translacao(x, y, tx, ty):
    
    x = float(x)
    y = float(y)
    tx = float(tx)
    ty = float(ty)
    mPont = np.array([  [x], [y], [1]   ])
    matriz = np.array([ [1, 0, tx], [0, 1, ty], [0, 0, 1]   ])
    
    mTrans = np.matmul(matriz, mPont)

    return mTrans

def escala(x, y, sx, sy):
    
    x = float(x)
    y = float(y)
    sx = float(sx)
    sy = float(sy)
    mPont = np.array([  [x], [y], [1]   ])
    matriz = np.array([ [sx, 0, 0], [0, sy, 0], [0, 0, 1]   ])
    
    mEsc = np.matmul(matriz, mPont)

    return mEsc

def rotacao(x, y, angulo):

    angulo = float(angulo)
    angulo = math.radians(angulo)

    cos = math.cos(angulo)
    sin = math.sin(angulo)
    
    x = float(x)
    y = float(y)

    mPonto = np.array([ [x], [y], [1]   ])
    matriz = np.array([ [cos, -sin, 0], [sin, cos, 0], [0, 0, 1] ])
    mRot = np.matmul(matriz, mPonto)     

    return mRot

def cisalhamento(x, y, kx, ky):

    x = float(x)
    y = float(y)
    kx = float(kx)
    ky = float(ky)
    
    newX = x + kx*y
    newY = y + ky*x

    arrayCis = [newX, newY]

    return arrayCis

def reflexao(x, y, eixo):

    x = float(x)
    y = float(y)
    
    if(eixo == 'x'):
        newX = x
        newY = -y
        
    elif(eixo == 'y'):
        newX = -x
        newY = y

    elif(eixo == 'y=x'):
        newX = y
        newY = x
        
    elif(eixo == 'y=-x'):
        newX = -y
        newY = -x

    mRefl = [newX, newY]
    return mRefl

# LETRA B
def rotacaoComposta(x, y, angulo, px, py):

    angulo = float(angulo)
    angulo = math.radians(angulo)
    cos = math.cos(angulo)
    sin = math.sin(angulo)
    x = float(x)
    y = float(y)
    px = float(px)
    py = float(py)

    t1 = np.array([ [1, 0, px], [0, 1, py], [0, 0, 1]])
    t2 = np.array([ [1, 0, -px], [0, 1, -py], [0, 0, 1]])
    matriz = np.array([[cos, -sin, 0], [sin, cos, 0], [0, 0, 1]])
    
    resultado = np.matmul(t1, matriz) 
    resultado = np.matmul(resultado, t2)

    ponto = np.array([  [x], [y], [1]])
    mRot = np.around(np.matmul(resultado, ponto), 2)
   
    return mRot


def escalaComposta(x, y, ex, ey, sx, sy):
    x = float(x)
    y = float(y)
    ex = float(ex)
    ey = float(ey)
    sx = float(sx)
    sy = float(sy)
    
    t1 = np.array([ [1, 0, ex], [0, 1, ey], [0, 0, 1]])
    matriz = np.array([ [sx, 0, 0], [0, sy, 0], [0, 0, 1]])
    t2 = np.array([ [1, 0, -ex], [0, 1, -ey], [0, 0, 1]])

    resultado = np.matmul(t1, matriz)
    resultado = np.matmul(resultado, t2)
    ponto = np.array([  [x], [y], [1]])
    mEsc = np.around(np.matmul(resultado, ponto), 2)
   
    return mEsc

def main():
    while True:
        print("1 - Translação")
        print("2 - Escala")
        print("3 - Rotação")
        print("4 - Cisalhamento")
        print("5 - Reflexão")
        print("6 - Rotação composta")
        print("7 - Escala em relação a um ponto")
        print("8 - Escala em relação ao ponto gemétrico")
        print("9 - Sair")

        op = input("\nOpção: ")

        print("\nDigite o ponto a ser modificado:")
        x = input("X: ")
        y = input("Y: ")

        op = int(op)
        if(op == 1):
            tx = input("Digite o X de translação: ")
            ty = input("Digite o Y de translação: ")
            result = translacao(x, y, tx, ty)
            print("\nPonto(x,y):", result[0][0], result[1][0])
            print("\n")

        if(op == 2):
            print("Digite o ponto de relação para a escala")
            sx = input("x: ")
            sy = input("y: ")
            result = escala(x, y, sx, sy)
            print("\nPonto(x,y):", result[0][0], result[1][0])
            print("\n")

        if(op == 3):
            angulo = input("Digite o angulo: ")
            result = rotacao(x, y, angulo)
            print("\nPonto(x,y):", result[0][0], result[1][0])
            print("\n")

        if(op == 4):
            cx = input("Digite o X para cisalhamento: ")
            cy = input("Digite o Y para cisalhamento: ")
            result = cisalhamento(x, y, cx, cy)
            print("\nPonto(x,y):", result)
            print("\n")
        
        if(op == 5):
            eixo = input("Digite o eixo para reflexão: ")
            result = reflexao(x, y, eixo)
            print("\nPonto(x,y):", result)
            print("\n")

        if(op == 6):
            angulo = input("Digite o angulo: ")
            print("Digite o ponto de relação para fazer a rotação")
            px = input("x: ")
            py = input("y: ")
            result = rotacaoComposta(x, y, angulo, px, py)
            print("\nPonto(x,y):", result[0][0], result[1][0])
            print("\n")

        if(op == 7):
            print("Digite o ponto de relação")
            ex = input("x: ")
            ey = input("y: ")
            print("Digite o valor de escala")
            sx = input("x: ")
            sy = input("y: ")
            result = escalaComposta(x, y, ex, ey, sx, sy)
            print("\nPonto(x,y):", result[0][0], result[1][0])
            print("\n")

        if(op == 8):
            print("Digite o valor de escala")
            sx = input("x: ")
            sy = input("y: ")
            result = escalaComposta(x, y, x, y, sx, sy)
            print("\nPonto(x,y):", result[0][0], result[1][0])
            print("\n")

        if(op == 9):
            print("Desculpa, não sei sair disso, tente novamente.")

main()
