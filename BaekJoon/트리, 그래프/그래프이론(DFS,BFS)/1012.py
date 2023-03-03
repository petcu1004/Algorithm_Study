## 유기농 배추

from collections import deque

case=int(input())



dx=[0, 0, -1, 1]
dy=[-1, 1, 0, 0]




def bfs(k):

    n=1
    q=deque()
    q.append(k)

    while(q):
        x, y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=a or ny<0 or ny>=b:
                continue

            if maps[nx][ny]==0:
                continue

            if maps[nx][ny]==1:
                n+=1
                maps[nx][ny]=0
                q.append((nx,ny))   

    return n
    


for _ in range(case):
    res=0
    a, b, c = map(int, input().split())
    maps=[]
    for i in range(a):
        maps.append([0]*b)

    for i in range(c):
        x, y = map(int, input().split())
        maps[x][y]=1
    for i in range(a):
        for j in range(b):
            if maps[i][j]==1:
                bfs((i, j))
                res+=1

    print(res)

