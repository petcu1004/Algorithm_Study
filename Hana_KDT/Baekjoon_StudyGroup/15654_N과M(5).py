from itertools import permutations

n, m= map(int, input().split())

arr=list(map(int, input().split(" ")))

# for i in sorted(permutations(arr, m)):
#     print(*i)

arr.sort()
visited=[0]*n
out=[]
#dfs
def solve(depth, n, m):
    if depth==m:
        print(' '.join(map(str, out)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i]=1
            out.append(arr[i])
            solve(depth+1, n, m)
            out.pop()
            visited[i]=0

solve(0, n, m)