# import sys
# n = int(input())

# graph = list()
# for i in range(n):
#     graph.append(list(map(int, input().split())))

# visited=[0 for _ in range(n)]
# min_diff=sys.maxsize #int(1e9) #최소값을 갱신할 변수 생성

# def dfs(depth, idx): #인덱스 변수를 인자로 받아준다.
#     global min_diff
#     if depth==n//2: # n은 늘 짝수로 주어진다고 했다. 주어진 수의 절반이 한 팀으로 선택되었을 떄 가지치기 시작
#         p1, p2 = 0, 0
#         for i in range(n):
#             for j in range(n):
#                 if visited[i] and visited[j]: # True의 값을 가지는 팀을 스타트팀이라 할때 스타트 팀의 능력치를 모두 p1에 더하고
#                     p1+=graph[i][j]
#                 elif not visited[i] and not visited[j]: # 나머지 절반 False의 값을 가지는 팀을 링크 팀이라 할때 링크 팀의 능력치를 모두 p2에 더한다.
#                     p2+=graph[i][j]
#         min_diff=min(min_diff, abs(p1-p2))
#         return

#     for i in range(idx, n): # 스타트 팀을 완성하지 못했을 때 백트래킹 실시
#         if not visited[i]:
#             visited[i]=1
#             dfs(depth+1, i+1) # 같은 번호 중복을 막기 위한 idx+1로 재귀호출
#             visited[i]=0

# dfs(0, 0)
# print(min_diff)


import sys
from itertools import combinations

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
members = list(range(n))  # 1 전체 멤버를 포함하는 리스트 생성
min_value = sys.maxsize  # 2 최소값을 비교할 변수 생성

for r1 in combinations(members, n // 2):  # 3 전체멤버의 절반을 r1으로 뽑아준다(스타트 팀)
    start, link = 0, 0
    r2 = list(set(members) - set(r1))  # 4 나머지 절반은 r2로 차집합해서 뺴준 뒤 리스트화 (링크팀)
    for r in combinations(r1, 2):  # 5 스타트팀에서 2명을 뽑아 팀의 능력치를 모두 더한다.
        start += graph[r[0]][r[1]]
        start += graph[r[1]][r[0]]
    for r in combinations(r2, 2):  # 6 링크팀에서 2명을 뽑아 팀의 능력치를 모두 더한다.
        link += graph[r[0]][r[1]]
        link += graph[r[1]][r[0]]
    min_value = min(min_value, abs(start - link))  # 7 한번의 r1으로 뽑는 조합이 끝날때마다 최소값 갱신
print(min_value)
