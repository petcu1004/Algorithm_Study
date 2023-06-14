import sys

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

visited = [0] * n
out = []

check = sys.maxsize


def dfs(depth, next, cost):
    global check

    if depth == n - 1 and arr[next][0] != 0:
        # arr[next][0]에서 0인 이유는 애초에 visited[0]=1로 해놔서 0을 시작하는 길이라고 생각했기 때문
        # 근데 0부터 방문으로 해도 되는건지.. 그걸 모르겠음. 1로 먼저 시작하면 같은 값이 나오기도 하지만 2와 3이라고 가정하고 코드를 바꾸면 다른 값이 나옴.
        # 다 방문했으면서, 마지막 도시에서 출발 도시로 가는 비용이 0이 아니라면(즉,갈수 있다면)
        check = min(check, cost + arr[next][0])
        return

    for i in range(n):
        if not visited[i] and arr[next][i] != 0:
            visited[i] = 1
            dfs(depth + 1, i, cost + arr[next][i])
            visited[i] = 0


visited[0] = 1
dfs(0, 0, 0)
print(check)
