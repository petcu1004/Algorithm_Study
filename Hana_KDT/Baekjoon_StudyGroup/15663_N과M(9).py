# from itertools import permutations
# import sys
# sys.setrecursionlimit(10**6)
# input=sys.stdin.readline

# n, m= map(int, input().split())

# arr=list(map(int, input().split(" ")))
# k=[]
# for i in sorted(permutations(arr, m)):
#     if i not in k:
#         print(*i)
#         k.append(i)
    

n, m= map(int, input().split())

arr=list(map(int, input().split(" ")))

arr.sort()
visited=[0]*n
out=[]
#dfs
def dfs(depth):
    check=0
    if depth==m:
        print(' '.join(map(str, out)))
        return
    for i in range(n):
        if not visited[i] and arr[i] != check:
            visited[i]=1
            check=arr[i]
            out.append(arr[i])
            dfs(depth+1)
            out.pop()
            visited[i]=0

dfs(0)