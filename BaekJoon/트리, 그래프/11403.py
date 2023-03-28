## 경로 찾기

n=int(input())

l=[]

for i in range(n):
    a=list(map(int, input().split()))
    l.append(a)

# print(l)
res=l

for k in range(n):
    # res[k][k]=1
    for i in range(n):
        for j in range(n):
            if res[i][k]==1 and res[k][j]==1:
                res[i][j]=1

# print(res)

for i in range(n):
    for j in range(n):
        print(res[i][j], end=' ')
    print()