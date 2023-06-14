import sys

input = sys.stdin.readline

# 우, 좌, 하, 상
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# INPUT
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

# 최대값 변수
maxValue = 0


# ㅗ, ㅜ, ㅓ, ㅏ 제외한 모양들 최대값 계산
def dfs(i, j, dsum, cnt):
    global maxValue
    # 모양 완성되었을 때 최대값 계산
    if cnt == 4:
        maxValue = max(maxValue, dsum)
        return

    # 상, 하, 좌, 우로 이동
    for n in range(4):
        ni = i + dx[n]
        nj = j + dy[n]
        if 0 > ni or ni >= N or 0 > nj or nj >= M:
            continue
        if visited[ni][nj]:
            continue

        if not visited[ni][nj]:
            visited[ni][nj] = 1
            dfs(ni, nj, dsum + board[ni][nj], cnt + 1)
            visited[ni][nj] = 0
        # if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]


# ㅗ, ㅜ, ㅓ, ㅏ 모양의 최대값 계산
def exce(i, j):
    global maxValue
    for n in range(4):
        # 초기값은 시작지점의 값으로 지정
        tmp = board[i][j]
        for k in range(3):
            # move 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # 012, 123, 230, 301
            t = (n + k) % 4
            ni = i + dx[t]
            nj = j + dy[t]

            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += board[ni][nj]
        # 최대값 계산
        maxValue = max(maxValue, tmp)


for i in range(N):
    for j in range(M):
        # 시작점 visited 표시
        visited[i][j] = 1
        dfs(i, j, board[i][j], 1)
        visited[i][j] = 0

        exce(i, j)

print(maxValue)
