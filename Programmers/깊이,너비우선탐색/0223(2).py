## 퍼즐 조각 채우기

from collections import deque

def solution(game_board, table):
    #상, 하, 좌, 우
    dx=[0, 0, 1, -1]
    dy=[1, -1, 0, 0]

    table_res=[]
    game_board_res=[]
    
    #https://bladejun.tistory.com/164
    def rotate(lst):
        n = len(lst)

        ret = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                ret[j][n-1-i] = lst[i][j]

        return ret

    
    
    
    def bfs(board,x, y, k):
        current_board = board
        r=[]
        q=deque()
        q.append((x, y))
        r.append((x-x, y-y)) #-x, -y 해준 이유는 0, 0에서 시작하는 것처럼 하기 위해
        
        while q:
            a, b = q.popleft()
            if k==1:
                current_board[a][b]=0
            else:
                current_board[a][b]=1
            
            
            
            # 상, 하, 좌, 우 확인
            for i in range(4):
                nx = a+dx[i]
                ny = b+dy[i]
                
                 # 칸 넘어가면 넘김
                if nx<0 or nx>=len(current_board) or ny<0 or ny>=len(current_board):
                    continue
                   
                # table에서 1인 블럭만 구해야 하기 떄문에 0인 경우 넘김 
                if current_board[nx][ny] != k: 
                    continue
                    
                # 처음 지나감
                if current_board[nx][ny]==k:
                    if k==1:
                        current_board[nx][ny]=0
                    else:
                        current_board[nx][ny]=1
                    # current_board[nx][ny] = 0
                    r.append((nx-x, ny-y)) #-x, -y 해준 이유는 0, 0에서 시작하는 것처럼 하기 위해
                    q.append((nx, ny))
                    
                    
        return r
    
    
    
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j]==1:
                table_res.append(bfs(table, i, j, 1))
                
    for a in range(len(game_board)):
        for b in range(len(game_board)):
            if game_board[a][b]==0:
                game_board_res.append(bfs(game_board, a, b, 0))             
    
    # for i in range(len(table_res)):
    #     for 
    
    print(table_res)
    print(game_board_res)
    
    ## 이렇게 나온 결과를 갖고 일단 맞는 블럭 있는지 확인하기 있다면 숫자 세고, 만약 없다면 rotate()함수 돌려서 또 다른 블럭 맞는지 없는지 확인해서 값 리턴하면 될듯.. 이때, 조각 맞춘 애들은 다시 안쓰이도록 방문 체크처럼 해줘야 함!

    
    # return answer