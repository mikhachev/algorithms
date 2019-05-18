''' 8 урок
Определить количество различных подстрок с использованием хеш-функции.
Задача: на вход функции дана строка, требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
'''
# Сравнить строки с помощью хеширования
import hashlib
import random
s=''
N = 100
for i in range(N):
    s += random.choice('abcdefghijklmnopqrstuvwxyz')


#s = 'aaab'
print(s)

#print(rabin_karp(s, 'r'))
#
def rabin_karp(s, len_sub):
    #cnt = 0
    t = s[:len_sub]
    h_subs = hashlib.sha1(t.encode('utf-8')).hexdigest()
    unic = []
    unic.append(h_subs)
    for i in range(len(s) - len_sub + 1):
        for pos in range(1, len(s)+1):
            if len_sub + pos > len(s):
                break
            h_subs = hashlib.sha1(s[pos : pos + len_sub].encode('utf-8')).hexdigest()
            if h_subs not in unic:
                unic.append(h_subs)

    return len(unic)


def not_hash(s, len_sub):
    # cnt = 0
    t = s[:len_sub]
    unic = []
    unic.append(t)
    for i in range(len(s) - len_sub + 1):
        for pos in range(1, len(s) + 1):
            if len_sub + pos > len(s):
                break
            h_subs = s[pos: pos + len_sub]
            if h_subs not in unic:
                unic.append(h_subs)

    return len(unic)

list = []
cnt = 0
cnt2 = 0
# i - длина подстроки
for i in range(1, len(s)):
    cnt += rabin_karp(s, i)
    cnt2 += not_hash(s, i)

print('Число различных подстрок в строке: ', cnt)
print('Точное число различных подстрок в строке: ', cnt2)
