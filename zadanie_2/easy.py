from itertools import product
imp = lambda a, b: not a or b

n = 3 # количество логических переменных
possibles = list(product((0,1), repeat=n))
expr = "" # ваше выражение

ans  = [list("xyzF")]
for i in possibles:
    x, y, z = i
    ans.append(x, y, z, eval(expr))
for i in ans:
    for j in i:
        print(f"{j: ^5}", end="")
 
    
