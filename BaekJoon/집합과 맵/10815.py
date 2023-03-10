## 숫자 카드 - 실버 5

# import sys
# sys.setrecursionlimit(10**6)
# input=sys.stdin.readline

# def binary(arr, value):
#     left, right = 0, n-1

#     while left <= right:
#         mid = (left+right)//2

#         if arr[mid]==value:
#             return 1
#         if arr[mid]>value:
#             right=mid-1
#         else:
#             left=mid+1
#     return 0

# n=int(input())
# a=list(map(int, input().split()))

# m=int(input())
# b=list(map(int, input().split()))

# a.sort()
# for i in b:
#     print(binary(a, i), end= ' ')

################################################

input()
n=set(map(int, input().split()))
input()
m=list(map(int, input().split()))
for i in m:
    if i in n:
        print(1, end=' ')
    else:
        print(0, end=' ')