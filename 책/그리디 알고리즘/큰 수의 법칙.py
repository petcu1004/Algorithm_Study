## 방법 1
# n, m, k = map(int, input().split())

# res=list(map(int, input().split()))

# res.sort()

# answer = 0
# for i in range(m):
#     a=res[-1]
#     b=res[-2]
#     if i%(k+1)==0:
#         answer+=b
#     else:
#         answer+=a

# print(answer)

#########################################
## 방법 2

n, m, k = map(int, input().split())

res=list(map(int, input().split()))

res.sort()
a=res[-1]
b=res[-2]

# 가장 큰 수가 더해지는 횟수 계산
cnt = int(m/(k+1)) *k
cnt+=m%(k+1)

answer = 0
answer+=(cnt)*a
answer+=(m-cnt) * b


print(answer)
