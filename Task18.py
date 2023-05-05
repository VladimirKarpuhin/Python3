import random
size = int(input('Введите размер списка: '))
min = 20
x = 0
my_list = [random.randint(0,20) for _ in range(size)]
print(my_list)
num = int(input('Введите искомое число: '))
for i in range(size):
    if abs(my_list[i]-num) < min:
        min = abs(my_list[i]-num)
        x = my_list[i]
print(f'Ближайшее значение к искомому числу: {x}')