## 별 찍기 - 2

n=int(input())

k='*'
for i in range(n):
    print(k.rjust(n, ' '))
    k+='*'

#또 다른 방법
for i in range(1, n+1):
    print(' '*(n-i) + '*' *i)