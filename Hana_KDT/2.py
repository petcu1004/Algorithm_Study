# n = int(input())

# a = list(map(int, input().split()))

# print(a)
# k=max(a)

# for i in a:
#     sum+=int(i)


n, m = map(int, input().split())

k = list(map(int, input().split()))
kk = [0]
# kk = list()
# 합 배열 구하는 중
for i in range(1, n + 1):
    kk[i] = kk[i - 1] + k[i - 1]


print(kk)


# for i in range(m):
#     a, b = map(int, input().split())
#     print(k[a])
