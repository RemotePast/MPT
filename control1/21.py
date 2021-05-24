# Принимает вес в килограммах и рост в метрах. Возвращает индекс массы тела. 
def bmi(weight: float, height: float):
    return weight / height**2

# Принимает численное значение ИМТ и печатает на экран соответствующую категорию
def print_bmi(bmi: float):
    if (bmi < 18.5):
        print('Underweight')
    elif (bmi >= 18.5 and bmi < 25.0):
        print('Normal')
    elif (bmi >= 25.0  and bmi < 30.0):
        print('Overweight')
    else:
        print('Obesity')

inp = input().split(' ')
weight = float(inp[0])
height = float(inp[1])/100
print_bmi(bmi(weight, height))