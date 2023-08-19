import math
import matplotlib.pyplot as plt
import time

def dda(x1, y1, x2, y2):
    step = math.fabs(x2 - x1)
    if(math.fabs(y2 - y1) > step):
        step = math.fabs(y2 - y1)
    xinc = (x2 - x1) / step
    yinc = (y2 - y1) / step
    x = x1
    y = y1

    plt.scatter(round(x), round(y), marker='o')
    while(x < x2):
        plt.scatter(round(x), round(y), marker='o')
        x+=xinc
        y+=yinc

    plt.show()

def bresenham_retas(x1, y1, x2, y2):
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if x1 < x2:
        sx = 1
    else:
        sx = -1

    if y1 < y2:
        sy = 1
    else:
        sy = -1    

    err = dy - dx
    
    while True:
        x1, y1

        if x1 == x2 or y1 == y2:
            break

        plt.scatter(x1, y1, marker='o')
        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x1 += sx

        if e2 < dx:
            err += dx
            y1 += sy

    plt.show()

def drawCircle(xc, yc, x, y):
    plt.scatter(xc+x, yc+y, marker='o', color='#FF0000')
    plt.scatter(xc-x, yc+y, marker='o', color='#FF0000')
    plt.scatter(xc+x, yc-y, marker='o', color='#FF0000')
    plt.scatter(xc-x, yc-y, marker='o', color='#FF0000')
    plt.scatter(xc+y, yc+x, marker='o', color='#FF0000')
    plt.scatter(xc-y, yc+x, marker='o', color='#FF0000')
    plt.scatter(xc+y, yc-x, marker='o', color='#FF0000')
    plt.scatter(xc-y, yc-x, marker='o', color='#FF0000')


def bresenhan_circunferencia(xc, yc, r):
    xc = int(xc)
    yc = int(yc)
    r = int(r)

    x = 0
    y = r
    d = 3 - (2 * r)

    drawCircle(xc, yc, x, y)

    while(y >= x):
        x += 1
        if (d > 0):
            y -= 1
            d += 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        drawCircle(xc, yc, x, y)
    plt.show()

def main():
    while True:
        print("1 - Algorimto DDA")
        print("2 - Bresenham para traçado de retas")
        print("3 - Bresenham para traçado de circunferências")
        print("4 - Sair")

        op = input("\nOpção: ")
        op = int(op)

        if(op == 1):
            x1 = float(input("X1: "))
            y1 = float(input("Y1: "))
            x2 = float(input("X2: "))
            y2 = float(input("Y2: "))
            dda(x1, y1, x2, y2)

        if(op == 2):
            x1 = int(input("X1: "))
            y1 = int(input("Y1: "))
            x2 = int(input("X2: "))
            y2 = int(input("Y2: "))
            bresenham_retas(x1, y1, x2, y2)

        if(op == 3):
            xc = int(input("XC: "))
            yc = int(input("YC: "))
            r = int(input("R: "))
            bresenhan_circunferencia(xc, yc, r)
        
        if(op == 4):
            print("Desculpa, não sei sair disso, tente novamente.")


main()



