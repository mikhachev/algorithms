# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.

import random
a = int(input('Введите 1-е целое число: '))
b = int(input('Введите 2-е целое число: '))
if a <= b:
    num = random.randint(a, b)
else:
    num = random.randint(b, a)
print(num)

a = float(input('Введите 1-е число: '))
b = float(input('Введите 2-е число: '))
if a <= b:
    num = random.uniform(a, b)
else:
    num = random.uniform(b, a)
print(num)

a = ord(input('Введите 1-ый символ: '))
b = ord(input('Введите 2-ый символ:: '))

if a <= b:
    num = random.randint(a, b)
else:
    num = random.randint(b, a)
print('Это символ', chr(num))




