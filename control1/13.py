number = int(input())
for i in range (2, number):
    if (number % i == 0):
        print("Составное")
        break
    elif (i == number - 1):
        print("Простое")
