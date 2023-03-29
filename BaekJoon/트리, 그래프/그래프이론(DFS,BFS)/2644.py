## 촌수계산
from collections import deque

n=int(input())
x, y = map(int, input().split())

martix=[[0]*(n+1) for _ in range(n+1)]
visited=[0]*(n+1)

k=int(input())
for i in range(k):
    a, b = map(int, input().split())
    martix[a][b] = martix[b][a] = 1

def bfs(v):
    