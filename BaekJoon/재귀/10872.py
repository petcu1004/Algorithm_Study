### for문
# res=1
# for i in range(1, int(input())+1):
#     res*=i
# print(res)

#-------------------------------------#
# n=1
# for i in range(int(input()), 1, -1):
#     n=n*i
# print(n)


#-------------------------------------#
### 재귀
n=int(input())
def factorial(n):
    if n<=1:
        return 1
    return n* factorial(n-1)

print(factorial(n))