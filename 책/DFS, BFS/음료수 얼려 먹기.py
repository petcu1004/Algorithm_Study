from collections import deque

n, m = map(int, input().split())

maps=[]
for i in range(n):
    maps.append(list(map(int, input())))

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def bfs(x, y):
    q=deque()
    q.append((x, y))
    maps[x][y]=1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=len(maps) or ny<0 or ny>=len(maps[0]):
                continue
            
            if maps[nx][ny]==0:
                maps[nx][ny]=1
                q.append((nx, ny))
    return 1


def dfs(x, y):
    
    if x<0 or x>=n or y<0 or y>=m:
        return 0
    if maps[x][y]==0:
        maps[x][y]=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            dfs(nx, ny)
        return 1
    return 0


cnt=0
for i in range(n):
    for j in range(m):
        if maps[i][j]==0:   
            cnt+=bfs(i, j)

        if dfs(i, j)==1:
            cnt+=1
            

print(cnt)