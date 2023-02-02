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



#피보나치 수열을 DP 문제로 해결.

dp = [0]*100 # 소문제 결과를 저장할 리스트
dp[0] = 1 
dp[1] = 1

def fib(n):
    
    # 만약 계산한 적이 없다면 재귀로 계산 
    if dp[n] == 0:
        dp[n] = fib(n-1) + fib(n-2)
    
    # 있다면 그대로 반환 
    return dp[n]

print(fib(10))
