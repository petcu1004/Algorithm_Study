import sys
from itertools import combinations

input = sys.stdin.readline


n, s = map(int, input().split())

arr = list(map(int, input().split()))
cnt = 0

visited = [0] * n

# 경우의 수를 다 구해야 함..(조합)
out = list()

# DFS로 푼 것


def dfs(depth, m, start):
    global cnt

    k = 0
    if depth == m:
        print(out)
        for i in range(m):
            k += out[i]
        if k == s:
            # print(out)

            cnt += 1
            return
    for i in range(start, n):
        if not visited[i]:
            out.append(arr[i])
            visited[i] = 1
            dfs(depth + 1, m, i + 1)
            visited[i] = 0
            out.pop()


for i in range(1, n + 1):
    dfs(0, i, 0)


print(cnt)


## 라이브러리로 푼 것
for i in range(1, n + 1):
    comb = combinations(arr, i)

    for k in comb:
        print(k)
        if sum(k) == s:
            cnt += 1

# print(cnt)
