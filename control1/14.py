n = int(input())
amount = 0

for i in range (0, n + 1):
    if (2 ** i <= n):
        amount += 1
    else:
        break
print(amount)