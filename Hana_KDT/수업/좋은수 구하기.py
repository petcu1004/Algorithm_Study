n = int(input())
a = list(map(int, input()))

a.sort()

for k in n:
    find = k
    i = 0
    j = n - 1
    while i < j:
        if a[i] + a[j] == find:
            if i not in k or j not in k:
                break
