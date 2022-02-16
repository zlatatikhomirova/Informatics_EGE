from itertools import product
from prettytable import PrettyTable

imp = lambda a, b: not a or b

n = 3 # количество логических переменных
possibles = list(product((0,1), repeat=n))
expr = "" # ваше выражение

def Btable(possibles: list):
        """
    Вывод таблички очень красивый.
    """
    mytable = PrettyTable()
    mytable.field_names = [list("xyzF")]
    for i in possibles:
        x, y, z = i
        mytable.add_row([x, y, z, eval(expr)])
    print(mytable)
    
def Etable(possibles: list):
    """
    Вывод таблички простой, не очень красивый.
    """
    ans  = [list("xyzF")]
    for i in possibles:
        x, y, z = i
        ans.append(x, y, z, eval(expr))
    for i in ans:
        for j in i:
            print(f"{j: ^5}", end="")

    
