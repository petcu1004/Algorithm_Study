## 최소 힙

import heapq
import sys
input=sys.stdin.readline

n=int(input())

h=[]
for i in range(n):
    x=int(input())
    if x==0:
        if len(h)==0:
            print(0)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, x)
    