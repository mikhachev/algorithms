#6. В одномерном массиве найти сумму элементов, находящихся между минимальным
# и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.


import random

RANGE_LENGTH = 10
list = []

for i in range(RANGE_LENGTH):
    list.append(random.randint(0, 100))
    if i == 1:
        if list[0] >= list[1]:
            min_index = 1
            max_index = 0
        else:
            min_index = 0
            max_index = 1
    elif i > 1:
        if list[i] > list[max_index]:
            max_index = i
        if list[i] < list[min_index]:
            min_index = i

sum = 0
if min_index > max_index:
    min_index, max_index = max_index, min_index
for i in range(min_index + 1, max_index):
    sum = sum + list[i]

print(list)
print(sum)










