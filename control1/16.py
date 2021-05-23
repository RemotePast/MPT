import re

n = int(input())
inp = input()
match_list = re.findall(r'a...55661', inp)
if (len(match_list) == 0):
    print("-1")   
else:
    for i in match_list:
        print(i, ' ')

