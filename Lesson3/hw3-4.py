# 4. Определить, какое число в массиве встречается чаще всего.
#P.S - без учета, что таких чисел может быть несколько

import random
list = []
uniq_list = []
amount = []
RANGE_LENGTH = 31
for i in range(RANGE_LENGTH):
    list.append(random.randint(0, 9))
    unique_number = True
    if i > 0:
        for y in range(i-1, -1, -1):
            if list[i] == list[y]:
                unique_number = False
        if unique_number  == True:
            uniq_list.append(list[i])
    else:
        uniq_list.append(list[0])


max = 1
for i in range(len(uniq_list)):
    amount.append(0)
    for y in range(RANGE_LENGTH):
        if list[y] == uniq_list[i]:
            amount[i] = amount[i] + 1
        if i > 0 and amount[i] > amount[i - 1]:
            max = i

print(list)
print(uniq_list)
print(amount)
print('Чаще всех встречается число: ', uniq_list[max])