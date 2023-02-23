#일곱 난쟁이

from itertools import combinations

arr=[]
for _ in range(9):
    a=input()
    arr.append(a)

b=list(combinations(arr,7))

res=0
for i in range(len(b)):
    c=[]
    res=0
    for j in range(7):
        x=int(b[i][j])
        res+=x
        c.append(x)
    if(res==100):
        c.sort()
        for j in range(7):
            print(c[j])
        break