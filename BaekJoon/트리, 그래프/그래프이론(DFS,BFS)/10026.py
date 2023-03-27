## 적록색약
from collections import deque

n=int(input())
res=[]

for i in range(n):
    k=input()
    res.append(list(k))

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]


def bfs(a, b, s, res):
    q=deque()
    q.append((a, b))

    while q:
        x, y=q.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=len(res) or ny<0 or ny>=len(res[0]):
                continue
            if res[nx][ny]!=s:
                continue
            else:
                res[nx][ny]=1
                q.append((nx, ny))

    return 1



answer=0
answer1=0
res1=[[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if res[i][j]=='G':
            res1[i][j]='R'
        else:
            res1[i][j]=res[i][j]

for i in range(n):
    for j in range(n):
        if res[i][j]!=1:
            answer+=bfs(i, j, res[i][j], res)
        if res1[i][j]!=1:
            answer1+=bfs(i, j, res1[i][j], res1)

print(answer, answer1)