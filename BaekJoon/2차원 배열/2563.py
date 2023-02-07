ip=int(input())
l = [[0 for j in range(100)] for i in range(100)] #0으로 초기화

for i in range(ip):
    x, y=map(int, input().split())
    for i in range(100):
        for j in range(100):
            if(i>=x and i<x+10) and (j>=y and j<y+10):
                l[i][j]+=1
k=0

for i in range(100):
    for j in range(100):
        if(l[i][j]>1):
            k+=l[i][j]-1

m=ip*100

print(m-k)