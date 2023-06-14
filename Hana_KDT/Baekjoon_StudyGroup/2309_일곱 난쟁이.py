from itertools import combinations

l = list()
for i in range(9):
    l.append(int(input()))

l.sort()

cb = list(combinations(l, 7))

res = 0
r = list()
for i in range(len(cb)):
    for j in range(7):
        res += cb[i][j]
        r.append(cb[i][j])
    if res == 100:
        break
    else:
        res = 0
        r = []

for i in range(7):
    print(r[i])
