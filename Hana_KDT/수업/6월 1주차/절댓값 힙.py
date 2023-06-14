import heapq
import sys

hq = []

input = sys.stdin.readline
n = int(input())
for i in range(n):
    a = int(input())
    if a == 0:
        if len(hq) == 0:  # if not hq라고 해도 됨.
            print(0)
        else:
            print(heapq.heappop(hq)[1])
    else:
        heapq.heappush(hq, (abs(a), a))


# 절댓값 처리.. 어떻게 하지 => abs()함수 사용

# from queue import PriorityQueue
# q=PriorityQueue()

# n=int(input())
# for i in range(n):
#     a=int(input())
#     if a==0:
#         if len(q)==0:
#             print(0)
#         else:
#             q.get()[1]
#     else:
#         q.put(a)
