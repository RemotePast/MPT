inp = input().split(' ')

try:
    a = float(inp[0])
    if (inp[1] == '+' or inp[1] == '-' or inp[1] == '*' or inp[1] == '/'):
        sign = inp[1]
    b = float(inp[2])
    if (sign == '+'):
        res = a + b
    elif (sign == '-'):
        res = a - b
    elif (sign == '*'):
        res = a * b
    else:
        res = a / b
    print(res)
except:
    print("Некорректный ввод.")