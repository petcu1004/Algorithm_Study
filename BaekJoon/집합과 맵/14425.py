## 문자열 집합

n, m = map(int, input().split())
res=0
a=set()
b=[]

for i in range(n):
    a.add(input())


for i in range(m):
    b.append(input())
    
for i in b:
    if i in a:
        res+=1

print(res)
