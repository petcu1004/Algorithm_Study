## 수 찾기

#이진탐색
# def binary(arr, value):
#     left = 0
#     right = len(arr)-1

#     while(left <= right):
#         mid = (left+right) //2
#         if arr[mid] == value:
#             return 1
#         elif  arr[mid] > value:
#             right=mid-1
#         else :
#             left=mid+1
#     return 0

# n= int(input())
# a=list(map(int,input().split(' ')))
# a.sort()
# m= int(input())
# b=list(map(int,input().split(' ')))

# for i in range(m):
#     print(binary(a, b[i]))

######################################################

#퀵정렬
n=int(input())
a=set(map(int, input().split())) #탐색 시간을 줄이기 위해 set으로 받음
m=int(input())
b=list(map(int, input().split()))

for i in b:
    if i in a:
        print(1)
    else :
        print(0)
