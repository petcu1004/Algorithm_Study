# from collections import deque

# # 상하좌우
# # 상(-1, 0) 하(1, 0) 좌(0, -1) 우(0, 1)
# dx=[-1, 1, 0, 0]
# dy=[0, 0, -1, 1]

# def bfs(x, y):
    
#     q=deque()
#     q.append((x, y))
#     maps[x][y]=0
#     k=1

#     while(q): # queue가 빌 때까지 반복
#         x, y=q.popleft()
        
#         for i in range(4):# 상하좌우 칸 확인하기
#             nx=x+dx[i]
#             ny=y+dy[i]

#             # 맵을 벗어나면 무시하기
#             if nx<0 or nx>=n or ny<0 or ny>=n:
#                 continue

#             # 처음 지나가는 길이면 거리계산하고 다시 상하좌우 확인하기
#             if maps[nx][ny] ==1:
#                 k+=1
#                 maps[nx][ny] = 0
#                 q.append((nx, ny))

#     return k


# n=int(input())
# maps=[]
# for i in range(n):
#     maps.append(list(map(int, input())))


# answer=[]

# for i in range(n):
#     for j in range(n):
#         if(maps[i][j]==1): #집이 있는 곳만 세기
#             answer.append(bfs(i, j))

# answer.sort() #오름차순으로 정렬

# print(len(answer))
# for i in range(len(answer)):
#     print(answer[i])

############################################

from collections import deque

# 상하좌우
# 상(-1, 0) 하(1, 0) 좌(0, -1) 우(0, 1)
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def dfs(x, y):
    
    if x<0 or x>=n or y<0 or y>=n:
        return 0

    if maps[x][y]==1:
        global k
        k+=1
        maps[x][y]=0
        for i in range(4):
            nx = x+dx[i]
            ny= y+dy[i]
            dfs(nx, ny) #재귀함수
        return 1
    return 0
    


n=int(input())
maps=[]
num=[]

for i in range(n):
    maps.append(list(map(int, input())))

k=0
result=0

for i in range(n):
    for j in range(n):
        if(dfs(i, j)==1): #집이 있는 곳만 세기
            num.append(k)
            result+=1
            k=0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])