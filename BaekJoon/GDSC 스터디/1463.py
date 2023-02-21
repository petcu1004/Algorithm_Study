# x=int(input())

# res=0
# while(x!=1):
#     if(x%3==0):
#         x//=3
#     elif(x%2==0):
#         x//=2
#     # elif(x==1):
#     #     break
#     else:
#         x-=1
#     print(x)
#     res+=1

# print(res)

n=int(input())
dp=[0] *(n+1)
for i in range(2, n+1):
    #0부터 시작하지 않는 이유는 다음에 계산할 나누기가 1을 뺀 값보다 작거나 큼에 따라 어차피 교체되기 때문이다.
    #즉 셋 다 시도하는 방법이 맞다.

    dp[i]=dp[i-1]+1
    if i%3==0:
        dp[i]=min(dp[i], dp[i//3] +1 ) #1을 더하는 이유는 dp는 결과가 아닌 계산한 횟수를 저장하기 때문이다. dp[i]에 더하지 않는 이유는 이미 1을 뺄 때 1을 더해준 이력이 있기 떄문
    if i%2==0:
        dp[i]=min(dp[i], dp[i//2] +1 )
print(dp[n])




#피보나치 수열을 DP 문제로 해결.

# dp = [0]*100 # 소문제 결과를 저장할 리스트
# dp[0] = 1 
# dp[1] = 1

# def fib(n):
    
#     # 만약 계산한 적이 없다면 재귀로 계산 
#     if dp[n] == 0:
#         dp[n] = fib(n-1) + fib(n-2)
    
#     # 있다면 그대로 반환 
#     return dp[n]

# print(fib(10))
