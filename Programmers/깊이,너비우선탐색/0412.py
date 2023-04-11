from collections import deque
def solution(maps):
    answer = 0
    dx=[-1, 1, 0, 0]
    dy=[0, 0, -1, 1]
    
    def bfs(x, y):
        q=deque()
        q.append((x, y))
        
        
        while(q):
            x, y=q.popleft()
            # maps[x][y]=0
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                
                if nx<0 or nx>=len(maps) or ny<0 or ny>=len(maps[0]):
                    continue
                if maps[nx][ny]==0:
                    continue
                    
                if maps[nx][ny]==1:
                    maps[nx][ny]=maps[x][y]+1
                    q.append((nx, ny))
                    
        return maps[len(maps)-1][len(maps[0])-1]

    if bfs(0, 0)==1:
        return -1
    else:
        return bfs(0, 0)
    
