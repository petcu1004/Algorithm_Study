n = int(input())

arr = list(map(str, input().split()))

visited = [0] * 10
out1 = ""  # 작은값 기준
out2 = ""  # 큰값 기준


def check(i, j, k):
    if k == "<":
        return i < j
    else:
        return i > j


def dfs(depth, s):
    print(s)
    global out1, out2
    if depth == n + 1:
        # 맨 처음 생성, 최소값
        if len(out1) == 0:
            out1 = s
        # 계속 대입, 마지막에는 최대값
        else:
            out2 = s
        return
    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(s[-1], str(i), arr[depth - 1]):
                visited[i] = 1
                dfs(depth + 1, s + str(i))
                visited[i] = 0


dfs(0, "")
print(out2)
print(out1)
