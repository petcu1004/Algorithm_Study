## 아이템 줍기

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    MAX = 102 # 두배로 늘리기 때문에 최대 102 (51*2)
    
    #테두리 그리기
    field = [[5] * MAX for _ in range(MAX)] #5는 맨처음 땅
    for rec in rectangle :
        x1, y1, x2, y2 = map(lambda x : x*2, rec) #각각 2배씩 늘림
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1<i<x2 and y1<j<y2: # 내부일 때
                    field[i][j] =0
                elif field[i][j] !=0: # 테두리일때 그리고 이미 내부가 아닐 때
                    field[i][j]=1 # 테두리랑 내부랑 겹치면 그건 내부
    
    # 길 찾기 (최단 거리는 BFS)
    q=deque()
    q.append([characterX *2, characterY *2])
    visited=[[0] * MAX for _ in range(MAX)]
    visited[characterX * 2][characterY * 2]=1
    dx=[1, -1, 0, 0]
    dy=[0, 0, 1, -1]
    
    while q:
        x, y = q.popleft()
        if x ==itemX *2 and y == itemY * 2:
            answer = (visited[x][y] -1) //2
            break
            
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if visited[nx][ny] ==0 and field[nx][ny] ==1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] +1
                        
    return answer