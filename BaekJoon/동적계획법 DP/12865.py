## 평범한 배낭 - 골드5

n, k = map(int, input().split())

res=[]
for i in range(n):
    a, b = map(int, input().split())
    res.append([a, b])
    
dp=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1, n+1):
        w=res[i][0]
        v=res[i][1]

        if j<w:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)