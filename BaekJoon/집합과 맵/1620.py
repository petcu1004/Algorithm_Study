## 나는야 포켓몬 마스터 이다솜 - 실버 4

import sys
input=sys.stdin.readline

n, m= map(int, input().split())

dogam={}

for i in range(1,n+1):
    k=input().rstrip() ##rstrip()을 해주지 않으면 /n까지 들어간다!!!
    dogam[i]=k
    dogam[k]=i

for i in range(m):
    x=input().rstrip()
    if x.isdigit():
        print(dogam[int(x)])
    else:
        print(dogam[x])