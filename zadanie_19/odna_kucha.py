# один или четыре камня либо увеличить количество камней в куче в пять раз.
N = 68
def f():
    prev = [lambda x: x+1, lambda x: x+4, lambda x: x*5]
    for s in range(100):
        for i in prev:
            for j in prev:
                if j(i(s)) >= N:
                    return (s, prev.index(i), prev.index(j))
