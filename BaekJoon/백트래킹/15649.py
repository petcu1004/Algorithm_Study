## N과 M (1)


n, m = map(int, input().split())

visited=[]

def dfs():

    if len(visited) == m:
        print(' '.join(map(str, visited)))

    for i in range(1, n+1):
        if i not in visited:
            visited.append(i)
            dfs()
            visited.pop()


dfs()
