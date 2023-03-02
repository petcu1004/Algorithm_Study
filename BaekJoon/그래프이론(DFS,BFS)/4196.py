## 도미노


import sys
sys.setrecursionlimit(10**6)
### 재귀를 사용해서 풀어야 하는 문제라면 이렇게 쓰는 것은 필수이다.
### 파이썬의 기본 재귀 깊이 제한은 1000으로 매우 얕은 편이다.
### 따라서 재귀로 문제를 풀 경우 드물지 않게 이 제한에 걸리게 된다. 이 함정에 걸린 사람은 원인 미상의 런타임 에러를 붙잡고 있게된다.

input = sys.stdin.readline

# 정방향 dfs, dfs 가 종료되는 노드를 stack에.
def dfs(node, visit, stack):
    visit[node] = 1
    for now in graph[node]:
        if visit[now] == 0:
            dfs(now, visit, stack)
    stack.append(node)

# 역방향 dfs, 탐색하는 순서대로 stack에.
def reverse_dfs(node, visit, stack):
    visit[node] = 1
    ids[node] = idx
    stack.append(node)
    for now in reverse_graph[node]:
        if visit[now] == 0:
            reverse_dfs(now, visit, stack)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    reverse_graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        x, y = map(int, input().split())
        # 정방향 그래프, 역방향 그래프 추가
        graph[x].append(y)
        reverse_graph[y].append(x)
    stack = []
    visit = [0] * (N + 1)
    # 모든 노드에서 dfs를 수행.
    for i in range(1, N + 1):
        if visit[i] == 0:
            dfs(i, visit, stack)
    idx = 0
    ids = [-1] * (N + 1)
    visit = [0] * (N + 1)
    result = []
    while stack:
        # pop되는 요소에서 역방향 dfs, scc를 결과에.
        ssc = []
        node = stack.pop()
        if visit[node] == 0:
            idx += 1
            reverse_dfs(node, visit, ssc)
            result.append(sorted(ssc))
    scc_indegree = [0] * (idx + 1)

    for i in range(1, N + 1):
        for ed in graph[i]:
            if ids[i] != ids[ed]:
                scc_indegree[ids[ed]] += 1
    cnt = 0
    for i in range(1, len(scc_indegree)):
        if scc_indegree[i] == 0:
            cnt += 1
    print(cnt)