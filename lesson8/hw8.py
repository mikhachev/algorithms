''' 8 урок
Определить количество различных подстрок с использованием хеш-функции.
Задача: на вход функции дана строка, требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.

N= 500
Число различных подстрок в строке методом sha1:  124621
Число различных подстрок в строке стандартным хешем питона :  124621
Точное число различных подстрок в строке:  124621
Время выполнения методом хэширования sha1  76.98313221012017
Время выполнения методом хэширования standart_hash(s)  29.539383627147117
Время выполнения методом хэширования not_hash(s)  30.18806733556039

N=100

Время выполнения методом хэширования sha1  0.5500707697025433
Время выполнения методом хэширования standart_hash(s)  0.1884853293209261
Время выполнения методом хэширования not_hash(s)  0.1684748110553116
Время выполнения методом хэширования sha1, но без set()  11.80773842049986


N=30
Время выполнения методом хэширования sha1  0.014141189210909233
Время выполнения методом хэширования standart_hash(s)  0.004512093361892122
Время выполнения методом хэширования not_hash(s)  0.00370191944352094
Время выполнения методом хэширования sha1, но без set() 0.03758398362360155

Выводы, мысли:
Намного медленнее всех метод без множеств, когда проверка уникальноси идет на каждом шаге.
Чем длиннее строка, тем это заметнее. На коротких строках он может быть даже быстрее,
видимо операция приведения к множеству тоже требует времени.
Среди алгоритмов с множеством хэширование sha1 значительно дольшн остальных, здесь проводится несколько операций.
Алгоритм без хеширования очень конкурентен, расчет хеша занимает время и лишь на длинных строках
более быстрый поиск окупается.

'''
# Сравнить строки с помощью хеширования
import hashlib
import random
import timeit
s=''
N = 30
for i in range(N):
    s += random.choice('abcdefghijklmnopqrstuvwxyz')


#s = 'aaab'
print(s)

#print(rabin_karp(s, 'r'))
#
def sha1(s):
    #cnt = 0
    unic = []
    for i in range(1, len(s)):
        t = s[:i]
        h_subs = hashlib.sha1(t.encode('utf-8')).hexdigest()

        unic.append(h_subs)
        for i in range(len(s) - i ):
            for pos in range(1, len(s) + 1):
                if i + pos > len(s):
                    break
                h_subs = hashlib.sha1(s[pos: pos + i].encode('utf-8')).hexdigest()
                #if h_subs not in unic:
                unic.append(h_subs)
    unic = set(unic)

    return len(unic)

def sha_without_set(s):
    #cnt = 0
    unic = []
    for i in range(1, len(s)):
        t = s[:i]
        h_subs = hashlib.sha1(t.encode('utf-8')).hexdigest()

        unic.append(h_subs)
        for i in range(len(s) - i ):
            for pos in range(1, len(s) + 1):
                if i + pos > len(s):
                    break
                h_subs = hashlib.sha1(s[pos: pos + i].encode('utf-8')).hexdigest()
                if h_subs not in unic:
                    unic.append(h_subs)


    return len(unic)

def standart_hash(s):
    #cnt = 0
    unic = []
    for i in range(1, len(s)):
        t = s[:i]
        h_subs = hash(t)
        unic.append(h_subs)
        for i in range(len(s) - i):
            for pos in range(1, len(s) + 1):
                if i + pos > len(s):
                    break
                h_subs = hash(s[pos: pos + i])
                # if h_subs not in unic:
                unic.append(h_subs)
    unic = set(unic)

    return len(unic)


def not_hash(s):
    # cnt = 0

    unic = []
    for i in range(1, len(s)):
        t = s[:i]
        unic.append(t)
        for i in range(len(s) - i ):
            for pos in range(1, len(s) + 1):
                if i + pos > len(s):
                    break
                h_subs = s[pos: pos + i]
                #if h_subs not in unic:
                unic.append(h_subs)

    unic = set(unic)
    return len(unic)

list = []
cnt = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
# i - длина подстроки
#for i in range(1, len(s)):
    #cnt += rabin_karp(s, i)
    #cnt2 += standart_hash(s, i)
    #cnt3 += not_hash(s, i)



#print(f"Пузырьковым методом сортировка выполнена за {bubble/5}")

print('Число различных подстрок в строке методом sha1: ', sha1(s))
print('Число различных подстрок в строке стандартным хешем питона : ', standart_hash(s))
print('Точное число различных подстрок в строке: ', not_hash(s))
print('Число различных подстрок в строке методом sha1 без set(): ', sha_without_set(s))

for i in range(5):
    cnt = timeit.timeit("sha1(s)", setup="from __main__ import sha1, s", number=1)
    cnt2 = timeit.timeit("standart_hash(s)", setup="from __main__ import standart_hash, s", number=1)
    cnt3 = timeit.timeit("not_hash(s)", setup="from __main__ import not_hash, s", number=1)
    cnt4 = timeit.timeit("sha_without_set(s)", setup="from __main__ import sha_without_set, s", number=1)
print(f"Время выполнения методом хэширования sha1  {cnt}")
print(f"Время выполнения методом хэширования standart_hash(s)  {cnt2}")
print(f"Время выполнения методом хэширования not_hash(s)  {cnt3}")
print(f"Время выполнения методом хэширования sha1, но без set() {cnt4}")





