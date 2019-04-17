# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

startnum = 32
def print_chr(startnum):
    str = chr(32)
    for i in range(startnum, startnum +11):
        if i > 127:
            break
        str = str + chr(i) + ' '
    return str

while startnum < 128:
    print(print_chr(startnum))
    startnum = startnum +10