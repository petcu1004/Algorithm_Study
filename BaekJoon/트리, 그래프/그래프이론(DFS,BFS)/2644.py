#촌수계산

from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v]=1

    while q:
        node=q.popleft()
        for i in range(1,n+1):
            if matrix[node][i]==1 and not visited[i]:
                q.append(i)
                res[i]=res[node]+1
                visited[i]=1

def dfs(v):
    visited[v]=1

    for i in range(1, n+1):
        if matrix[v][i]==1 and not visited[i]:
            res[i]=res[v]+1
            dfs(i)

n=int(input())
x, y = map(int, input().split())

matrix=[[0]*(n+1) for _ in range(n+1)]
visited=[0]*(n+1)
res=[0]*(n+1)

k=int(input())
for i in range(k):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

               
dfs(x)
if res[y]>0:
    print(res[y])
else:
    print(-1)