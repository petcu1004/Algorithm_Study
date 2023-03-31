## 연구소
from collections import deque
from itertools import combinations
import copy

n,m = map(int, input().split())

maps=[]
for i in range(n):
    k=list(map(int, input().split()))
    maps.append(k)

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

def bfs(mm):
    ans=0
    q=deque()

    # 바이러스가 퍼져나가면 나오는 결과
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=len(mm) or ny<0 or ny>=len(mm[0]):
                continue
            if mm[nx][ny]==1 or mm[nx][ny]==2:
                continue
            if mm[nx][ny]==0:
                q.append((nx, ny))
                mm[nx][ny]=2

    for i in range(n):
        for j in range(m):
            if mm[i][j]==0:
                ans+=1
                
    return ans

#벽을 3개 세워야 함.
root=[]
for i in range(n):
    for j in range(m):
        if maps[i][j]==0:
            root.append((i, j))

answer=0
# print(root)
for k in list(combinations(root, 3)):
    tmp=copy.deepcopy(maps)
    # print(k)
    for i in range(3):
        tmp[k[i][0]][k[i][1]]=1
    # print(tmp)

    # # 바이러스가 퍼져나가면 나오는 결과
    # for i in range(n):
    #     for j in range(m):
    #         if tmp[i][j]==2:
    #             # print("바이러스 개수")
    #             print(tmp)
    answer=max(answer,bfs(tmp))
                # if answer!=32:
                #     print(answer)
                    
                # print(bfs(tmp, i, j))

# print(tmp)



# answer=0
# for i in range(n):
#     for j in range(m):
#         if tmp[i][j]==2:
#             answer=max(answer,bfs(tmp, i, j))

print(answer)