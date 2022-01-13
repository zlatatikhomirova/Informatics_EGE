# добавить в одну из куч (по своему выбору) один камень или увеличить количество камней в куче в два раза.

prev = [lambda x: x+1, lambda x: x*2]
for s in range(100):
	heaps = [7, s]
	for i in prev:
		for j in prev:
			if j(i(s)) >= 68:
				return (s, prev.index(i), prev.index(j))
