## DFS와 BFS

# 입력 변수 받기
node, edge, start  = map(int, input().split())

# 인접 영행령 생성
matrix = [[0] *(node+1) for i in range(node+1)]
    
# 방문한 곳 체크를 위한 배열 선언
visited=[0] * (node +1)

# 입력 받는 두 값에 대해 영행렬에 1 삽입
for i in range(edge):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] =1

def dfs(v):
    # 방문한 곳은 1 넣기
    visited[v]=1

    print(v, end=' ')

    # 재귀 함수 선언 (start와 인접한 곳을 찾고 방문하지 않았다면 함수 실행)
    for i in range(1, node+1):
        if(visited[i]==0 and matrix[v][i]==1):
            dfs(i)


def bfs(v):
    # 방문해야 할 곳을 순서대로 넣을 큐
    queue=[v]

    # dfs를 완료한 visited 배열 (1로 되어있음)에서 방문 체크
    visited[v]=0

    # 큐 안에 데이터가 없을 때까지
    while queue:
        v=queue.pop(0)
        print(v, end=' ')
        for i in range(1, node+1):
            if(visited[i]==1 and matrix[v][i] ==1):
                queue.append(i)
                visited[i]=0


dfs(start)
print()
bfs(start)