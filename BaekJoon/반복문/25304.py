### 영수증

n=int(input())
cnt=int(input())

res=0
for i in range(cnt):
    a,b = map(int, input().split())
    res+=(a*b)

if res==n:
    print("Yes")
else:
    print("No")
