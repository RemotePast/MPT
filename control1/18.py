word_list = ['hallo', 'klempner', 'das', 'ist', 'fantastisch', 'fluggegecheimen']
dic = {}   
word_line = ("".join(word_list))
sum = 0

for i in word_line:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
    sum += 1
for i in dic:
    prob = dic[i] / sum
    dic[i] = prob

stop_word = input()
prob = 1
for i in stop_word:
    if (i in dic):
        prob *= dic[i]
    else:
        prob = 0
        break
print(prob)
