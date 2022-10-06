# Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной
# части элементов. минимальное значение дробной части отличное от нуля,
# у целых чисел дробной части нет их в расчет не берем
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

    # Первое решение

from random import randint

n = int(input('Enter the quantity of numbers in list: '))
list = []
coefficient = 1.123
for i in range(n):
    list.append(round(randint(1, 10) * coefficient, 2))
print(list)
print()

min = 1
max = 0
for i in list:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)  

print(f'Разница между max и min значением дробной части элементов: {round(max - min, 2)}')




    # Второе решение

from random import randint

n = int(input('Enter the quantity of numbers in list: '))
lst = []
coefficient = 1.123
for i in range(n):
    lst.append(round(randint(1, 10) * coefficient, 2))
print(lst)
print()

lst = list(map(lambda x: round(x - int(x), 2), lst))
print(f'Разница между max и min значением дробной части элементов: {max(lst) - min(lst)}')