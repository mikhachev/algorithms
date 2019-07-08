# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

RANGE_LENGTH = 10
list = []

for i in range(RANGE_LENGTH):
    list.append(random.randint(0, 100))
    if i == 1:
        if list[0] >= list[1]:
            min = list[1]
            not_min = list[0]
        else:
            min = list[0]
            not_min = list[1]
    elif i > 1:
        if list[i] <= min:
            not_min = min
            min = list[i]



print(list)
print('Минимальные числа:', min, not_min)
