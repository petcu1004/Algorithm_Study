## A+B - 7

import sys

input=sys.stdin.readline
n=int(input())

for i in range(n):
    a, b= map(int, input().split())
    # print("Case #", end='')
    # print(i+1, end='')
    # print(":", end=' ')
    # print(a+b)

    print(f'Case #{i+1}: {a+b}')
    
    # print("Case #", i+1, ": ", a+b, sep='')