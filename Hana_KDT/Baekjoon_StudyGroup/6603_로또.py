def dfs(depth, start):
    if depth == 6:
        print(" ".join(map(str, out)))
        return
    for i in range(start, len(arr)):
        # 조합으로 순서가 다른 리스트로 같은 조합인것! 그래서 처음 방문한 값은 다신 방문하지 않아야 함.
        out.append(arr[i])
        dfs(depth + 1, i + 1)
        out.pop()


while 1:
    arr = list(map(int, input().split()))
    k = arr[0]
    arr = arr[1:]
    out = []
    dfs(0, 0)
    if k == 0:
        exit()
    print()
