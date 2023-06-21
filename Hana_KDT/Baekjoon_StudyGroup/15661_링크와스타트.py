import sys

input = sys.stdin.readline
from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
new_S = [sum(i) + sum(j) for i, j in zip(S, zip(*S))]
total_S = sum(new_S) // 2

m = sys.maxsize
for i in range(1, N):
    for c in combinations(new_S[1:], i):
        m = min(m, abs(total_S - sum(c)))
        if not m:
            break
    if not m:
        break
print(m)

# import sys
# input=sys.stdin.readline

# n=int(input())
# stats = [list(map(int, input().split())) for i in range(n)]

# visited=[0]*n
# ans=99999

# def is_it():
#     global ans
#     start, link =0, 0
#     for i in range(n):
#         for j in range(n):
#             if visited[i] and visited[j]:
#                 start +=stats[i][j]
#             elif not visited[i] and not visited[j]:
#                 link+=stats[i][j]
#     ans=min(ans, abs(start-link)) #최소값 갱신
#     return

# # DFS (가능한 조합을 모두 뽑아줘야 헀음)
# def resolve(iter):
#     if iter ==n:
#         is_it()
#         return
#     visited[iter]=1
#     resolve(iter+1)
#     visited[iter]=0
#     resolve(iter+1)

# resolve(0)

# print(ans)
