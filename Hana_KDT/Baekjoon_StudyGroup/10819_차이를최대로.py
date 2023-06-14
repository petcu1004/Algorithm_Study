from itertools import permutations

n=int(input())
arr=list(map(int, input().split(" ")))

res=0
for i in permutations(arr):
    k=0
    for j in range(1,n):
        k+=abs(i[j-1]-i[j])
    if res<k:
        res=k
print(res)
