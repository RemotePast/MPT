#выбор способа расчета
#1 - ввод параметров треугольника через длины сторон
#2 - ввод параметров через координаты вершин
import math
method = int(input())
if (method == 1):
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("S = " + str(S))
elif (method == 2):
    xy1 = input().split(' ')
    x1 = float(xy1[0])
    y1 = float(xy1[1])
    
    xy2 = input().split(' ')
    x2 = float(xy2[0])
    y2 = float(xy2[1])
    
    xy3 = input().split(' ')
    x3 = float(xy3[0])
    y3 = float(xy3[1])
    
    S= 0.5 * math.fabs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3))
    print("S = " + str(S))
else:
    print("Было введено некорректное значение.")