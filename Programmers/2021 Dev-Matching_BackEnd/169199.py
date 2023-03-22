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
                nx, ny = x, y #처음 정해진 길로 쭈욱 미끄러지기 때문에 while문에서는 처음 큐에서 들어가는 값에서 시작해서 한 방향으로 가게

                if board[nx][ny]=='G':
                            print("찾음")
                            # print(k)
                            return v[x][y]
                while(1):    
                    nx=nx+dx[i] #nx = x+dx[i]이 안되는 이유) 한 방향으로 쭉 미끄러져야 하기 때문에 만약 
                    ny=ny+dy[i]
                    print(dx[i], dy[i])
                    print(nx, ny)

                    # if board[nx-dx[i]][ny-dy[i]]=='G': #while문 안쪽에 못넣는 이유는 while에서는 일단 한칸씩 이동하는걸로 되는데 쭈욱 미끄러지다가 멈추는 곳에서 도착했는지를 봐야하는데 while문안에 있으면 그렇지 못하기 때문이다.
                    #         print("찾음")
                    #         print(k)
                    #         return k

  
                    if nx>=len(board) or nx<0 or ny>=len(board[0]) or ny<0:
                        print("나감")
                        nx-=dx[i]
                        ny-=dy[i]
                        # q.append((nx-dx[i], ny-dy[i]))
                        # k+=1
                        # print(v)
                        break

                    if board[nx][ny]=='D' : #장애물을 만났을 때
                        print("장애물")
                        nx-=dx[i]
                        ny-=dy[i]
                        # q.append((nx-dx[i], ny-dy[i]))
                        # v[nx][ny]=1
                        # k+=1
                        # print(v)
                        break
                    
                    # if board[nx][ny]=='.' or board[nx][ny]=='R' or board[nx][ny]=='G' and v[nx][ny]==0: #빈공간일때
                    #     print("빈공간")
                    #     print(nx, ny)

                    #     if board[nx+dx[i]][ny+dy[i]]=='D':
                    #         print("다음 장애물 있음")
                    #         v[nx][ny]=1
                            
                    #         q.append((nx, ny))
                    #         break
                    #         # if v[nx][ny]:
                    #         #     break
                            
                            
                    #         print(v)
                    #         continue

                    #     v[nx][ny]=1
                    #     x=nx
                    #     y=ny
                    #     continue
                    # else: #
                    #     x=nx
                    #     y=ny
                    #     break
                if not v[nx][ny]: #쭉 미끄러지고 나서 그 지점을 체크해서 +1을 더해주는 것이다.
                    # k+=1
                    v[nx][ny]=v[x][y]+1
                    q.append((nx, ny))
        return -1

           
    result=bfs(a, b)
    if result>0:
         return result-1

    return result               
            
        
    



k= ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]

# for i in k:
#     print(i)
print(solution(k))