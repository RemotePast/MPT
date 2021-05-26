import json

output = []

with open('in.json', 'r', encoding='utf-8') as f:
    text = json.load(f)
    for i in text:
        if ({"userId" : i['userId'], "task_completed" : 0} not in output):
            output.append({"userId" : i['userId'], "task_completed" : 0})
    for i in text:
        if i['completed'] == True:
            for j in output:
                if (j['userId'] == i['userId']):
                    j['task_completed'] += 1         
            
with open('out.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)
    