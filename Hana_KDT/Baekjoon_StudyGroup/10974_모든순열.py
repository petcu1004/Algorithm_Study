from itertools import permutations

n = int(input())
arr = list()
for i in range(1, n + 1):
    arr.append(i)

for j in permutations(arr, n):
    print(*j)


def dfs(depth):
    global ans

    if depth == n:
        print(*visited)
    else:
        for i in range(n):
            if i + 1 in visited:
                continue
            visited[depth] = i + 1
            dfs(depth + 1)
            visited[depth] = 0


n = int(input())
visited = [0] * n
dfs(0)
