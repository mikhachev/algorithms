# №2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random
list = []
second_list = []
amount = []
RANGE_LENGTH = 10
for i in range(RANGE_LENGTH):
    list.append(random.randint(0, 100))
    if list[i] % 2 == 0:
        second_list.append(list[i])

print(list)
print(second_list)