# 단어 뒤집기

import sys
input=sys.stdin.readline

t=int(input())
for i in range(t):
    a=list(input().split())
    res=""
    for j in range(len(a)):
        k=list(a[j])
        result=list(reversed(k))
        res+="".join(result)+" "
    print(res)
        
