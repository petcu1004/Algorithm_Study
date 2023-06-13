from itertools import product

n, m= map(int, input().split())

arr=list(map(int, input().split(" ")))

for i in sorted(product((arr), repeat=m)):
    print(*i)
