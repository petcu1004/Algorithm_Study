import sys

input = sys.stdin.readline
ip = int(input())


def add(n):
    dp = [0] * (n + 3)  # 이 부분이 중요한 듯..
    # 기본값
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    if n < 4:
        return dp[n]

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


for i in range(ip):
    k = int(input())
    print(add(k))
