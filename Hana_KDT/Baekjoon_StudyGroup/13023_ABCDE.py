n, m = map(int, input().split())

relations = [[] for _ in range(n)]

visited = [0] * 2001  # 방문 체크

ans = 0  # 성공 표시 변수

for i in range(m):
    a, b = map(int, input().split())
    # 친구 관계 등록
    relations[a].append(b)  # a와 연결되어 있는 친구들 추가
    relations[b].append(a)


def dfs(depth, idx):
    global ans
    visited[idx] = 1

    if depth == 4:  # 친구 관계가 4번 이상 연결되어 있다면
        ans = 1  # 성공 표시 후 리턴
        return

    for i in relations[idx]:  # 친구 관계가 존재하는 지 확인
        if not visited[i]:
            visited[i] = 1
            dfs(depth + 1, i)
            visited[i] = 0


for i in range(n):
    # 친구 관계 탐색
    dfs(0, i)
    visited[i] = 0
    if ans:
        break

if ans:
    print(1)
else:
    print(0)
