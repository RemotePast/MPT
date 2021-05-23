try:
    time1 = input().split(':')
    h1 = float(time1[0])
    m1 = float(time1[1])

    time2 = input().split(':')
    h2 = float(time2[0])
    m2 = float(time2[1])

    dif = (h2 * 60 + m2) - (h1 * 60 + m1)
    if (dif <= 15):
        print("\nВстреча состоится")
    else:
        print("\nВстреча не состоится")
except:
    print("\nНекорректный ввод")