import random
size = int(input('Введите размер списка: '))
count = 0
my_list = [random.randint(0,20) for _ in range(size)]
print(my_list)
num = int(input('Введите искомое число: '))
for i in range(size):
    if my_list[i] == num:
        count += 1
print(f'Число {num} встречается в списке {count} раз.')