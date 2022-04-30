"""
Ссылка на задание: https://inf-ege.sdamgia.ru/problem?id=39253

Примечание к решению:
первая функция - самостоятельно написанное решение,
а вторая - эталонное решение с РЕШУ ЕГЭ, переписаннное с Pascal на Python.
"""

def f(text):
    k = 0
    best = 0
    c = 0
    prev = 0
    prev_len = 0

    for j, cur in enumerate(text):
        if  cur == "D":
            k += 1
            if k > 1:
                best = max(c, best)
                c = c - prev + 2
                k = 1
                prev = c + 1
                continue
        c += 1

    print(best)


def h(text):
    best = 0
    cur_len = 0
    k = 0
    c = 0
    for cur in text:
        c += 1
        if cur != 'D':
            cur_len += 1
            if cur_len > best:
                best = cur_len
        elif k == 0:
            k = 1
            i = c
            cur_len += 1
            if cur_len > best:
                best = cur_len
        elif k == 1:
            cur_len = c - i
            i = c
            if cur_len > best:
                best = cur_len

    print(best)

with open("24.txt", "r") as text:
    text = text.read().strip()
    f(text)
    h(text)
