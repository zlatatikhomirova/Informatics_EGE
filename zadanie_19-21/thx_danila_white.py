"""
Функция `winpos` возвращает True если игрок находится в выигрышной позиции,
False - если он в ней не находитися.

`count1` - количество камней в 1-й куче;
`count2` - количество камней в 2-й куче.

Если изначально суммарное количество камней в кучах меньше 61
if (count1 + count2 < 61)
и при любом следующем ходе оно становится больше либо равно 61
((count1 + count2 + 1 >= 61) or
(count1 * 4 + count2 >= 61) or 
(count1 + count2 * 4 >= 61)),
то мы возвращаем True, ведь игрок находится в выигрышной позиции, иначе - False.
"""

def winpos(count1, count2):
    if (count1 + count2 < 61) and ((count1 + count2 + 1 >= 61) or
       (count1 * 4 + count2 >= 61) or (count1 + count2 * 4 >= 61)):
        return True
    else:
        return False
      
"""
Функция возвращает True, если игрок находится в проигрышной позиции и False если игрок не находится в проигрышной позиции.

Если изначально игрок не находиться в выигрышной позиции
if not winpos(count1, count2)
и каждый следующий ход противника является выигрышным
(winpos(count1 + 1, count2) and winpos(count1, count2 + 1) and
 winpos(count1 * 4, count2) and winpos(count1, count2 * 4))
то мы возвращаем True, что означает что игрок находиться в проигрышной позиции.
Иначе, мы возвращаем False, что означает что игрок не находиться в проигрышной позиции.
"""
def losspos(count1, count2):
    if not winpos(count1, count2) and (winpos(count1 + 1, count2) and
        winpos(count1, count2 + 1) and winpos(count1 * 4, count2) and
        winpos(count1, count2 * 4)):
        return True
    else:
        return False
"""
Вторая функция готова, осталась еще одна.

Prewinpos
Последняя функция должна возвращать True если игрок находится в предвыигрышной позиции и False если игрок не находится в предвыигрышной позиции.

Если изначально игрок не находится в выигрышной позиции
if not winpos(count1, count2)
и любой следующий ход противника является проигрышным
(losspos(count1 + 1, count2) or losspos(count1, count2 + 1) or
 losspos(count1 * 4, count2) or losspos(count1, count2 * 4)):
то мы возвращаем True, что означает что игрок находится в предвыигрышной позциии.
Иначе, мы возвращаем False, что означает что игрок не находиться в предвыигрышной позциии.
"""
def prewinpos(count1, count2):
    if not winpos(count1, count2) and (losspos(count1 + 1, count2) or
        losspos(count1, count2 + 1) or losspos(count1 * 4, count2) or
        losspos(count1, count2 * 4)):
        return True
    else:
        return False
Основа готова, осталось просто перебрать значения, чем мы сейчас и займемся.

1 Задача
Условие задачи можно воспринимать так: "Ваня находиться в выигрышной позиции(выигрывает за один ход)".

Изначально в первой куче 3 камня
count1 = 3
а во второй куче S камней, 1 ≤ S ≤ 57
for s in range(1, 58):
Перебираем все возможные комбинации с S, при которых игрок находится в выигрышной позиции
if winpos(count1 + 1, s) or winpos(count1, s + 1) or
   winpos(count1 * 4, s) or winpos(count1, s * 4):
и если хоть одна такая комбинация существует, то мы выводим S на экран и прерываем цикл.
print("19:", s)
break
Получается следующий код, который решает эту задачу
count1 = 3
for i in range(1, 58):
    if winpos(count1 + 1, i) or winpos(count1, i + 1) or
        winpos(count1 * 4, i) or winpos(count1, i * 4):
        print("19:", i)
        break
2 Задача
Условие задачи можно воспринимать так: "Ваня находится в проигрышной позиции".

Перебираем все возможные комбинации с S, при которых игрок находиться в проигрышной позиции, и если такие комбинации существуют, то мы выводим S на экран
for i in range(1, 58):
    if losspos(count1 + 1, i) or losspos(count1, i + 1) or
        losspos(count1 * 4, i) or losspos(count1, i * 4):
        print("20:", i)
3 Задача
Условие задачи можно воспринимать так: "Ваня находиться или в выигрышной или в предвыигрышной позиции"

Перебираем все возможные комбинации с S, при которых игрок находиться или в выигрышной или в предвыигрышной позиции, и если такие комбинации существуют, то мы выводим S на экран
if (winpos(count1 + 1, i) or predwinpos(count1 + 1, i)) and 
   (winpos(count1, i + 1) or predwinpos(count1, i + 1)) and 
   (winpos(count1 * 4, i) or predwinpos(count1 * 4, i)) and 
   (winpos(count1, i * 4) or predwinpos(count1, i * 4)):
   print("21:", i)
2 Способ
Подробней с этим методом решения теории игр вы можете ознакомится на канале Алексея Кабанова

Мемоизация
Для оптимизации рекурсии подключим декоратор cache из модуля functools.
from functools import cache
Moves
Напишем функцию moves, которая принимает количество камней в обеих кучах и возвращает всевозможные варианты ходов.
def moves(heap):
    a, b = heap
    return (a + 1, b), (a * 4, b), (a, b + 1), (a, b * 4)
Game
Напишем функцию game, которая рекурсивно описывает игру.
@cache
def game(heap):
    if sum(heap) >= 61:
        return 0
    steps = [game(x) for x in moves(heap)]
    if any(x % 2 == 0 for x in steps):
        return min(x for x in steps if x % 2 == 0) + 1
    else:
        return max(steps) + 1
1-3 задача
Перебираем все значения s и выводим на экран необходимые данные.
for s in range(57, 0, -1):
    print(s, ": ", game((3, s)), " | ", [game(x) for x in moves((3, s))])
На выходе мы получаем полное дерево игры, в котором можно увидеть ответы на поставленные задачи.
