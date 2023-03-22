## 리코쳇 로봇

from collections import deque

def solution(board):
    answer = 0
    
    for i in range(len(board)):
        if not board[i].index('R'):
            continue
        else:
            a=i
            b=board[i].index('R')
            break
    # print(a, b)
    
    
    #상 하 좌 우
    dx = [-1, 1, 0, 0] #행 이동
    dy = [0, 0, -1, 1] #열 이동
    

    # v = [[0]*len(board[0])]*len(board)
    v = [[0]*len(board[0]) for _ in range(len(board))]
    # print(v)   
    # v[1][6]=1
    # print(v)
   

    def bfs(x, y):
        k=1
        q=deque()
        q.append((x, y))
        v[x][y]=1
        print(q)
        
        while(q):

            d=q.popleft()
            x=d[0]
            y=d[1]
            
            for i in range(4):
                
                while(1):    
                    nx=x+dx[i]
                    ny=y+dy[i]
                    print(dx[i], dy[i])
                    print(nx, ny)

                    if board[nx-dx[i]][ny-dy[i]]=='G':
                            print("찾음")
                            print(k)
                            return k

                    if board[nx][ny]=='D' : #장애물을 만났을 때
                        if board[nx-dx[i]][ny-dy[i]]=='G':
                            print("찾음")
                            print(k)
                            return k
                        print("장애물")
                        q.append((nx-dx[i], ny-dy[i]))
                        v[nx][ny]=1
                        k+=1
                        print(v)
                        break
                        
                    if nx>=len(board) or nx<0 or ny>=len(board[0]) or ny<0:
                        print("나감")
                        q.append((nx-dx[i], ny-dy[i]))
                        k+=1
                        print(v)
                        break
                    
                    if board[nx][ny]=='.' or board[nx][ny]=='R' or board[nx][ny]=='G' and v[nx][ny]==0: #빈공간일때
                        print("빈공간")
                        print(nx, ny)

                        if board[nx+dx[i]][ny+dy[i]]=='D':
                            print("다음 장애물 있음")
                            v[nx][ny]=1
                            
                            q.append((nx, ny))
                            break
                            # if v[nx][ny]:
                            #     break
                            
                            
                            print(v)
                            continue

                        v[nx][ny]=1
                        x=nx
                        y=ny
                        continue
                    else: #
                        x=nx
                        y=ny
                        break
                  


                        
           
                    
                
                    
    bfs(a, b)                
            
        
        
    
    return -1



k= ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]

for i in k:
    print(i)
print(solution(k))