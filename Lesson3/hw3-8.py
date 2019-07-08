# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки
# и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу

import random

M = 5
N = 4
list = []
for i in range(M):
    cell = []
    sum = 0
    for j in range(N):
        num = random.randint(0, 100)
        sum = sum + num
        cell.append(num)
    cell.append(sum)
    list.append(cell)

for i in list:
    print(i)
