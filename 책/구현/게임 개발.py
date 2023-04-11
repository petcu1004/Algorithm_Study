#방법 1 - 정답 코드

n, m = map(int, input().split())

visited=[[0]*m for _ in range(n)]

x, y, c = map(int, input().split())
visited[x][y]=1


#북, 동, 남, 서
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

maps=[]
for i in range(n):
    maps.append(list(map(int, input().split())))

#왼쪽으로 회전
def turn_left():
    global c
    c-=1
    if c==-1:
        c=3

# 시뮬레이션 시작
count=1
turn_time=0
while (1):
    turn_left()
    nx=x+dx[c]
    ny=y+dy[c]
    if visited[nx][ny] ==0 and maps[nx][ny] ==0: #방문하지 않았으면서, 육지인 곳이라면
        visited[nx][ny]=1 # 방문 체크
        x=nx #이동
        y=ny #이동
        count+=1 
        turn_time = 0 #이동한 곳에서 다시 회전 체크
        continue
    else:
        turn_time+=1
    if turn_time ==4: #모든 방향 체크했는데 갈 곳이 없는 경우
        nx=x-dx[c] #그 방향에서 뒤로 한 칸 가고자 함.
        ny=y-dx[c]
        if maps[nx][ny]==0: #육지인 경우
            x=nx #뒤로 이동
            y=ny
        else: #바다인 경우
            break #이제 어디로든 못가니까 break
        turn_time=0

print(count)


###########################################################

#방법 2 - 위 코드에서 수정함. (맞는지는 모르겠음)

# n, m = map(int, input().split())

# x, y, c = map(int, input().split())



# #북, 동, 남, 서
# dx=[-1, 0, 1, 0]
# dy=[0, 1, 0, -1]

# maps=[]
# for i in range(n):
#     maps.append(list(map(int, input().split())))

# maps[x][y]=1

# #왼쪽으로 회전
# def turn_left():
#     global c
#     c-=1
#     if c==-1:
#         c=3

# # 시뮬레이션 시작
# count=1
# turn_time=0
# while (1):
#     turn_left()
#     nx=x+dx[c]
#     ny=y+dy[c]
#     if maps[nx][ny] ==0: #방문하지 않았으면서, 육지인 곳이라면
#         maps[nx][ny]=1 # 방문 체크
#         x=nx #이동
#         y=ny #이동
#         count+=1 
#         turn_time = 0 #이동한 곳에서 다시 회전 체크
#         continue
#     else:
#         turn_time+=1
#     if turn_time ==4: #모든 방향 체크했는데 갈 곳이 없는 경우
#         nx=x-dx[c] #그 방향에서 뒤로 한 칸 가고자 함.
#         ny=y-dx[c]
#         if maps[nx][ny]==0: #육지인 경우
#             x=nx #뒤로 이동
#             y=ny
#         else: #바다인 경우
#             break #이제 어디로든 못가니까 break
#         turn_time=0

# print(count)

