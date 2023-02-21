# 바이러스

from collections import deque

num=int(input())

edge = int(input())

matrix = [[0]*(num+1) for _ in range(num+1)] ##방문 체크할 리스트

visited=[0]*(num+1)

for _ in range(edge):
    a, b=map(int, input().split()) 
    matrix[a][b]=matrix[b][a]=1

def bfs(i):
    answer=0
    q=deque()
    q.append(i)

    visited[i]=1

    while q:
        x=q.popleft()
        for i in range(1, num+1):
                if not visited[i] and matrix[x][i]==1:
                    q.append(i)
                    answer+=1
                    visited[i]=1

    return answer

root_node=1
print(bfs(root_node))