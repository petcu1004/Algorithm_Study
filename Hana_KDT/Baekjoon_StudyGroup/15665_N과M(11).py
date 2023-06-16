n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

visited = [0] * n
out = []
depth = 0


def dfs(depth):
    check = 0
    if m == depth:
        print(" ".join(map(str, out)))
        return
    for i in range(n):
        if not visited[i] and arr[i] != check:
            # visited[i] = 1
            check = arr[i]
            out.append(arr[i])
            dfs(depth + 1)
            out.pop()
            # visited[i] = 0


dfs(0)
