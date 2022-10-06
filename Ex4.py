# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

dec_number = int(input('Enter integer number: '))
bi_number = ''
while dec_number > 0:
    if dec_number % 2 == 0:
        bi_number = '0' + bi_number
    else:
        bi_number = '1' + bi_number
    dec_number //= 2
print()
print(f'Binary code of a number is: {bi_number}')