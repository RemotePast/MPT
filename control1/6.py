import math
a = float(input(""))
b = float(input(""))
c = float(input(""))

if (a == 0):
    if (b == 0):
        if (c == 0):
            print("\nКорнями являются все действительные числа.") 
        else: 
            print("\nДействительных корней нет.")
    else:
        if (c == 0):
            print("\nx = 0") 
        else: 
            print("\nx = " + str(-c / b))
else:
    if (b == 0):
        if (c == 0):
            print("\nx = 0")
        else: 
            print("\nx = " + str(math.sqrt(-c / a)))
    else:
        if (c == 0):
            print("\nx1 = 0")
            print("\nx2 = " + str(-b / a))
        else:
            D = b**2 - (4 * a *c)
            if (D > 0):
                print("\nx1 = " + str((-b + math.sqrt(D)) / 2 * a))
                print("\nx2 = " + str((-b - math.sqrt(D)) / 2 * a))
            elif (D == 0):
                print("\nx1, x2 = " + str((-b - math.sqrt(D)) / 2 * a))
            else:
                print("\nДействительных корней нет.")
    