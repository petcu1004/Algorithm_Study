n, m, v = map(int, input().split())

matrix = [[0] * (n + 1) for i in range(n + 1)]

visited = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1


def dfs(v):
    visited[v] = 1

    print(v, end=" ")

    for i in range(1, n + 1):
        # 방문 안했고, 인접한 곳이라면
        if visited[i] == 0 and matrix[v][i] == 1:
            dfs(i)


def bfs(v):
    q = [v]

    # dfs를 완료한 visited 배열 (1로 되어있음)에서 방문 체크
    visited[v] = 0

    while q:
        v = q.pop(0)
        print(v, end=" ")
        for i in range(1, n + 1):
            if visited[i] == 1 and matrix[v][i] == 1:
                q.append(i)
                visited[i] = 0


dfs(v)
print()
bfs(v)
