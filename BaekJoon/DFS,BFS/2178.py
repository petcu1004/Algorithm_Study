## 미로 탐색
from collections import deque

a, b = map(int, input().split())
maps=[]

for i in range(a):
    maps.append(list(map(int, input())))

dx=[0, 0, -1, 1]
dy=[-1, 1, 0, 0]


def bfs(k):

    q=deque()
    q.append(k)

    while q:
        x, y=q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0>nx or nx>=a or 0>ny or ny>=b:
                continue

            if maps[nx][ny]==0:
                continue

            if maps[nx][ny]==1:
                maps[nx][ny] = maps[x][y]+1
                q.append((nx, ny))
            
    return maps[a-1][b-1]

print(bfs((0, 0)))