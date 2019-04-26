# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

import collections

n = int(input("Количество предприятий: "))

firms={}
totalprofit = 0
GMBH = collections.namedtuple('GMBH', ['name', 'profit1', 'profit2', 'profit3', 'profit4'])
for i in range(n):

    name = input(str(i+1) + "название предприятия: ")
    profit1 = int(input("Прибыль за 1 квартал: "))
    profit2 = int(input("Прибыль за 2 квартал: "))
    profit3 = int(input("Прибыль за 3 кварт1ал: "))
    profit4 = int(input("Прибыль за 4 квартал: "))
    #name = 'asfd'
    #profit1 = 12
    #profit2 = 15
    #profit3 = 12
    #profit4 = 30
    firms[i] = GMBH(name, profit1, profit2, profit3, profit4)

    totalprofit += profit1 + profit2 + profit3 + profit4

avg = totalprofit/n
print("\nСредняя годовая прибыли предприятия: %.2f :" % avg)
print("\nПредприятия с прибылью выщше средней")

for i in firms:
    if firms[i].profit1 + firms[i].profit2 + firms[i].profit3 + firms[i].profit4 >= avg:
        print(firms[i].name)

print("\nПредприятия с прибылью ниже средней")

for i in firms:
    if firms[i].profit1 + firms[i].profit2 + firms[i].profit3 + firms[i].profit4 < avg:
        print(firms[i].name)
