arr = input().split(" ")
x0 = float(arr[0])
v0 = float(arr[1])
t = float(arr[2])

g = 9.8

x = x0 + v0 * t + (g * (t**2)) / 2
print(str(x))