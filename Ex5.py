# Задайте число. Составьте список чисел Фибоначчи, в том числе для
# отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

number = int(input('Enter integer number: '))
fib = [0, 1]

for i in range(1, number):
    fib.append(fib[i] + fib[i - 1])

nega_fib = fib[::-1]

for i in range(0, number-1, 2):
    nega_fib[i] = -nega_fib[i]

nega_fib.pop(number)

print(nega_fib + fib)