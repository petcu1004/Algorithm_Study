n, m = map(int, input().split())

k=0
for i in range(n):
    a=list(map(int, input().split()))
    
    res=min(a)

    answer=max(res, k)


print(answer)