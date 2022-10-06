# Задайте число. Составьте список чисел Фибоначчи, в том числе для
# отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fib(number):
    if number in (1, 2):
        return 1
    return fib(number-1) + fib(number-2)


n = int(input('Enter integer number: '))
nega_fib = [0]

for i in range(1, n+1):
    nega_fib.append(-fib(i))
    nega_fib.append(fib(i))
nega_fib.sort()
print(nega_fib)