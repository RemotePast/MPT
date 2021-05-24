n = 1
k = 0
l = list()
unused = list()
for i in range(0, 37):
    unused.append(i)
max_count_list = list()
max_count = 0
red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
red_count = 0
black_count = 0
while True: 
    n = int(input())
    if (n < 0):
        break
    if (k < 12):
        k += 1
    else:
        del_element = l[0]
        del l[0]
        if (del_element not in l):
            unused.append(del_element)
            unused.sort()
        if del_element in red:
            red_count -= 1
        else:
            black_count -= 1
        max_count_list.clear()
        max_count = 0
    l.append(n)
    
    for i in l:
        if (l.count(i) > max_count):
            max_count = l.count(i)
            max_count_list.clear()
            max_count_list.append(i)
        elif (l.count(i) == max_count and i not in max_count_list):
            max_count_list.append(i)
    max_count_list.sort()
    
    print(" ".join(map(str, max_count_list)))
    for i in l:
        for j in unused:
            if (i == j):
                unused.remove(i)
    print(" ".join(map(str, unused)))
    
    if (l[-1] in red):
        red_count += 1
    else:
        black_count += 1
    print(str(red_count) + " " + str(black_count) + '\n')