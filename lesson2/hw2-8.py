
# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def find_number(digit, num):
    digit_in_number = 0

    while num > 0:
        b = num % 10
        num = num // 10

        if b == digit:
            digit_in_number = digit_in_number + 1
    return digit_in_number

n = int(input("Введите количество чисел: "))
digit = int(input("Введите цифру для поиска: "))

digit_in_number = 0
for num in range(n):
    num = int(input("Введите очередное число: "))
    digit_in_number = digit_in_number + find_number(digit, num)

print(digit_in_number)








