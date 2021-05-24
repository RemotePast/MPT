from itertools import product as pr

n = int(input())
k = input()
print('\n')
k = list(k)
comb_w_repeats = []
for i in pr(k, repeat=n):
    comb_w_repeats.append(list(i))
comb = comb_w_repeats.copy()
for i in range(0, len(comb_w_repeats)):
    for j in range(0, len(k)):
        if k[j] not in comb_w_repeats[i]:
            comb.remove(comb_w_repeats[i])
            break
for i in comb:
    print("".join(i))
    