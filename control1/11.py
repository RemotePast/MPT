number = float(input())
power = int(input())
res = number
for i in range(1, power):
    res *= number
print(res)