# На основе зажачи 2-7.  
#  апишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+1/4+...+(1/4)**n = 4/3, при n стремящемся к бесконечности.

# n = int(input("Введите количество элементов прогрессии: "))

import timeit

REPEAT = 10000

def  with_forrange(n):
    sum = 0
    exp = n * (n + 1) / 2
    for i in range(n+1):
        sum += (1/4)**i
        #sum = sum + (1/4)**i

    return sum


def  with_while(n):
    i = 0
    sum = 0
    exp = n * (n + 1) / 2
    while i <= n:
        sum += (1/4)**i
        i = i + 1
        #sum = sum + (1/4)**i
    return sum

def recur(n):
   if n < 1:
      return 1

   return recur(n-1) + (1/4)**n

#print(recur(n))
n = 2
while n <= 1000:
    print("%0.15f" % with_forrange(n),
          "%0.3f" % timeit.timeit("with_forrange(n)", setup="from __main__ import with_forrange, n", number=REPEAT),
          "%0.3f" % timeit.timeit("with_while(n)", setup="from __main__ import with_while, n", number=REPEAT), 
          "%0.3f" % timeit.timeit("recur(n)", setup="from __main__ import recur, n", number=REPEAT))
    n = n*10
