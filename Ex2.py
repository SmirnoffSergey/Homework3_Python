# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint

n = int(input('Enter the quantity of numbers in list: '))
list = []

for i in range(n):
    list.append(randint(-10, 10))
print(list)
print()

result_list = []
for i in range((len(list) + 1)// 2):
    result_list.append(list[i] * list[-i-1])
print(f'The multi of pairs of numbers (example: the first * the last) is: \n{result_list}')
