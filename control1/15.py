from random import randint

i = 1
while (i <= 5):
    if (i == 1):
        print("{Приветственное сообщение от игры}")
        n = randint(0, 100)
    guess = int(input())
    if (guess < n):
        print("Загаданное число больше")
    elif (guess == n):
        print("Поздравляю! Вы угадали")
        decision = int(input("Хотите начать сначала? (1 - ДА ): "))
        if (decision == 1):
            i = 1
            continue
        else:
            break
    elif (guess > n):
        print("Загаданное число меньше")
    print(n)
    if (i == 5):
        print("Вы проиграли. Было загадано: " + str(n))
        decision = int(input("Хотите начать сначала? (1 - ДА )"))
        if (decision == 1):
            i = 1
            continue
        else:
            break
    else:
        i += 1