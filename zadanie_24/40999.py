"""
Ссылка на задание: https://inf-ege.sdamgia.ru/problem?id=40999

"""
def f(text):
    k = 0
    best = 0
    c = 0

    for cur in text:
        if  cur == "E":
            c = 0
            k = 0
            continue
        if cur == "A":
            k += 1
        c += 1
        if k >= 3:
            best = max(c, best)

    print(best)

with open("24.txt", "r") as text:
    text = text.read().strip()
    f(text)
