def fact(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return num * fact(num - 1)


number = int(input())
print(fact(number))
