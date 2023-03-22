## 리코쳇 로봇

from collections import deque

def solution(board):
    
    n=len(board)
    m=len(board[0])
    
    for i in range(n):
        for j in range(m):
            if board[i][j]=='R':
                a, b = i, j
    
    #상 하 좌 우
    dx = [-1, 1, 0, 0] #행 이동
    dy = [0, 0, -1, 1] #열 이동
    

    # v = [[0]*len(board[0])]*len(board) #이렇게 작성하면 XX
    v = [[0]*m for _ in range(n)]

    def bfs(x, y):
        q=deque()
        q.append((x, y))
        v[x][y]=1
        
        while(q):
            x, y=q.popleft()
            
            for i in range(4): 
                nx, ny = x, y #처음 정해진 길로 쭈욱 미끄러지기 때문에 while문에서는 처음 큐에서 들어가는 값에서 시작해서 한 방향으로 가게

                if board[nx][ny]=='G':
                            return v[x][y]
                while(1):    
                    nx=nx+dx[i] #nx = x+dx[i]이 안되는 이유) 한 방향으로 쭉 미끄러져야 하기 때문에 만약 
                    ny=ny+dy[i]

                    if nx>=n or nx<0 or ny>=m or ny<0:
                        nx-=dx[i]
                        ny-=dy[i]
                        break

                    if board[nx][ny]=='D' : #장애물을 만났을 때
                        nx-=dx[i]
                        ny-=dy[i]
                        break
                    
                if not v[nx][ny]: #쭉 미끄러지고 나서 그 지점을 체크해서 +1을 더해주는 것이다.
                    v[nx][ny]=v[x][y]+1
                    q.append((nx, ny))
        return -1

           
    result=bfs(a, b)
    if result>0:
         return result-1

    return result 