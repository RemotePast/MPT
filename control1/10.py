try:
    inp = input().split(' ')
    s = int(inp[0])
    l1 = int(inp[1])
    r1 = int(inp[2])
    l2 = int(inp[3])
    r2 = int(inp[4])
    if (s - l1 >= l2 and s - l1 <= r2):
        x1 = l1
        x2 = s - l1
        print(str(x1) + ' ' + str(x2))
    elif (s - l1 < l2 and 2 * l1 + l2 - s <= r1 and 2 * s - 2 * l1 - l2 >= l2 and 2 * s - 2 * l1 - l2 <= r2):
        x1 = 2 * l1 + l2 - s
        x2 = s - x1
        print(str(x1) + ' ' + str(x2))
    else:
        print("-1")
except:
    print("-11")
