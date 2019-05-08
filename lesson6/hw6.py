# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.

# На основе задачи 2-5: Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

from pympler import asizeof
import numpy as np


startnum = 32


def print_chr(startnum):
    str = chr(32)
    mem = 0
    #mem += asizeof.asizeof(chr(32))
    for i in range(startnum, startnum +10):
        if i > 127:
            break
        str = str + chr(i) + ' '
        #str = chr(i) + ' '
        #print(asizeof.asizeof(str))
    mem = asizeof.asizeof(str)
       #return str
    return mem


def print_list_chr(startnum):
    str = chr(32)
    mem = 0
    #mem += asizeof.asizeof(chr(32))

    list=[]

    for i in range(startnum, startnum +10):

        if i > 127:
            break
        list.append(chr(i))
    return asizeof.asizeof(list)


def print_tuple_chr(startnum):
    str = chr(32)
    mem = 0
    #mem += asizeof.asizeof(chr(32))

    line=''
    for i in range(startnum, startnum +10):

        if i > 127:
            break
        line += chr(i)
    kortez = tuple(line)
    print(kortez)
    return asizeof.asizeof(kortez)


def print_set_chr(startnum):
    str = chr(32)
    mem = 0
    #mem += asizeof.asizeof(chr(32))

    line=''
    nabor = set()
    for i in range(startnum, startnum +10):

        if i > 127:
            break
        line += chr(i)
        nabor.add(chr(i))

    nabor = set(line)
    #print(asizeof.asizeof(nabor))
    return asizeof.asizeof(nabor)

def print_numpylist_chr(startnum):
    str = chr(32)
    mem = 0
    #mem += asizeof.asizeof(chr(32))

    list=np.array([])

    for i in range(startnum, startnum +10):

        if i > 127:
            break
        list = np.append(list, chr(i))
    #print(list)
    #print(asizeof.asizeof(list))

    return asizeof.asizeof(list)



mem = asizeof.asizeof(startnum)
mem2 = asizeof.asizeof(startnum)
mem3 = asizeof.asizeof(startnum)
mem4 = asizeof.asizeof(startnum)
mem5 = asizeof.asizeof(startnum)



# Перебираем все решения выше и вычисляем расход памяти
while startnum < 128:
    mem += print_chr(startnum)
    mem2 += print_list_chr(startnum)
    mem3 += print_tuple_chr(startnum)
    mem4 += print_set_chr(startnum)
    mem5 += print_numpylist_chr(startnum)
    #print(print_chr(startnum))
    startnum = startnum +10


print('Байт выделено под решение с циклом: ', mem)
print('Байт выделено под решение с одномерным массивом: ', mem2)
print('Байт выделено под решение с кортежем: ', mem3)
print('Байт выделено под решение с множеством: ', mem4)
print('Байт выделено под решение с numpy массивом: ', mem5)


# Для сравнения оценим разные структуры данных без алгоритмов:
list = ['a', 'b', 'c']
list2=np.array(['a', 'b', 'c'])
nabor = set(list)
numpylist = np.array([])
numpylist = np.append(numpylist, 'a')
numpylist = np.append(numpylist, 'b')
numpylist = np.append(numpylist, 'c')

print('массив: ',asizeof.asizeof(list))
print('множество: ',asizeof.asizeof(nabor))
print('numpy массив: ',asizeof.asizeof(list2))
print('numpy массив c добавлением элементов: ',asizeof.asizeof(numpylist))

''' 
Результат:
Байт выделено под решение с циклом:  488
Байт выделено под решение с одномерным массивом:  4096
Байт выделено под решение с кортежем:  3792
Байт выделено под решение с множеством:  6848
Байт выделено под решение с numpy массивом:  12784
массив:  144
множество:  216
numpy массив:  64
numpy массив c добавлением элементов:  432 ['a' 'b' 'c']

Версия Python: 3.7
Windows 7 64 bit

Выводы:
Задача была изначально решена оптимальным образом через циклы, разница с другими решениями на порядок.
Решение со списком и кортежем сравнимо по объему памяти.

Внизу кода я для сравнения и проверки вывел, сколько съедается памяти на этих же структурах в простом варианте. 
Это пришлось сделать, поскольку полученные результаты были для меня частично неожиданными.

Set не годится для этой задачи, т.к. перемешивает данные, но все равно проверил расход памяти. 
Изначально было ожидание, что это более простая структура и будет меньше расход, чем со списком. 
На деле он оказался вдвое более затратным. Вероятно дело в том, что set использует хэш,
который следит, чтобы хотя бы половина таблицы была не заполнена.


Самый удивительный для меня был результат с numpy-массивом. Изначально ожидал, что раз numpy написан на С,
он будет более экономичным. В задаче он оказывается самым неэкономичным, а при проверке вдвое более 
экономичным, чем список. Нашел, что в целом да, numpy экономичнее и еще более быстрые, но операция добавления элементов
в numpy уже затратна и append отрабатывает гораздо лучше. 
https://stackoverflow.com/questions/46860970/why-use-numpy-over-list-based-on-speed
Проверка подтвердила эту гипотезу.

C memory_profiler поработал, но сделал вывод что его нужно использовать при большом количестве данных, 
на задачах из ДЗ он не показателен.



'''





