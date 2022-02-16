from itertools import product

def imp(a, b):
    """
    Импликация двух высказываний ложна тогда и только тогда, когда из истинного высказывания следует ложное.
    
    +---+---+-------+
    | A | B | A → B |
    +---+---+-------+
    | 0 | 0 |   1   |
    | 0 | 1 |   1   |
    | 1 | 0 |   0   |
    | 1 | 1 |   1   |
    +---+---+-------+
    
    Код:
    
    if a and not b:
        return 0
    return 1
    
    или
    
    return not a or b
    """
    return not a or b

def to_py(expr: str) -> str:
    """
    Функция преобразует исходное выражение в выражение, которое воспринимается интерпретатором Python.
    Поддерживает большинство логических операций, кроме импликации, стрелок Пирса, штриха Шеффера.
    
    Импликацию пропишем вручную.
    """
    log_operations = {'¬': " not ", '∧': " and ", '∨': " or ", '≡': " == ", '⊻': '^', '⊕': '^'} 
    for el in log_operations:
        try:
            expr.replace(el, log_operations[el])
        except KeyError:
            continue
    return expr

def log_table(n: int, params: list, expr: str) -> PrettyTable:
    """
    n - количество переменных в логическом выражении.
    params - переменные в логическом выражении.
    expr - выражение, которое нужно вычислить.
    """
    possible_values = list(product((0,1), repeat=n))
    
    

txt = """0	0	0	0
0	0	1	1
0	1	0	0
0	1	1	1
1	0	0	0
1	0	1	0
1	1	0	0
1	1	1	1"""

check = []

for elem in txt.split('\n'):
  check.append([int(i) for i in elem.split('\t')])

print(check)

n = 3 # количество переменных


statement = "(¬x ∧ y ∧ z) ∨ (¬x ∧ ¬y ∧ z) ∨ (¬x ∧ ¬y ∧ ¬z)"
# log_operations = {'¬': " not ", '∧': " and ", '∨': " or ", '→': "!", '≡': " == ", '⊻': '^', '⊕': '^'}  
# tbl = statement.maketrans(log_operations)
# expr_default = statement.translate(tbl)
del_log = {a[0]: '' for a in log_operations.items()}
tbl_1 = statement.maketrans(del_log)
chr_d = statement.translate(tbl_1)

chars = set(chr_d.replace(')', '').replace('(', ''))
chars.remove(' ')
chars = list(chars)
k=1
# if k == n : break
tmp_chars = [chars[(i+k)%len(chars)] for i in range(len(chars))]

#if ans == check:
# print_result(ans)
possible_values = list(product((0,1), repeat=n))
ans = [chars+['F']]

for values in possible_values:
  expr = expr_default
  for i, value in enumerate(values):
    expr = expr.replace(ans[0][i], str(value))
  ans.append(list(values)+[eval(expr)])
  

for i in range(len(ans)):
  for j in range(len(ans[0])):
    print(f"{ans[i][j]:<4}", end=" ")
  print()

  
