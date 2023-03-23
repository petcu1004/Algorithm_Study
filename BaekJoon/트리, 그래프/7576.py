## 토마토
from collections import deque


m, n = map(int, input().split())
board=[]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

for i in range(n):
    k=list(map(int, input().split()))
    board.append(k)

q=deque()

for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            q.append((i, j))

# print(board)

def bfs():
    while(q):
        x, y = q.popleft()
        # print(x, y)

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # print(nx, ny)

            if 0>nx or nx>=len(board) or 0>ny or ny>=len(board[0]):
                continue
            if board[nx][ny] == 0:
                board[nx][ny]=board[x][y]+1
                q.append((nx, ny))
        
    
# print(bfs())
bfs()
res=0
for i in range(n):
    for j in range(m):
        if board[i][j]==0:
            print(-1)
            exit(0)
        res=max(board[i][j], res)
print(res-1)
