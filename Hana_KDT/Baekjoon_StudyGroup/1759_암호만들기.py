a, b = map(int, input().split())

arr = list(input().split())

arr.sort()
visited = [0] * b
out = []


def dfs(depth, start):
    x = 0
    y = 0
    if depth == a:
        for i in range(a):
            if out[i] in ["a", "e", "i", "o", "u"]:
                x += 1
            else:
                y += 1
        if x >= 1 and y >= 2:
            print("".join(out))
        return
    else:
        for i in range(start, b):
            if not visited[i]:
                out.append(arr[i])
                visited[i] = 1
                dfs(depth + 1, i + 1)

                out.pop()
                visited[i] = 0


dfs(0, 0)
