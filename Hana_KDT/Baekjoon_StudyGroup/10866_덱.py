# 덱
import sys
input=sys.stdin.readline

n=int(input())

deque=list()
for i in range(n):
    a=input().split()

    if a[0]=="push_front":
        deque.insert(0, a[1])
    elif a[0]=="push_back":
        deque.insert(-1, a[1])
    elif a[0]=="pop_front":
        if len(deque)==0:
            print(-1)
        else:
            print(deque.pop(0))
    elif a[0]=="pop_back":
        if len(deque)==0:
            print(-1)
        else:
            print(deque.pop(-1))
    elif a[0]=="size":
        print(len(deque))
    elif a[0]=="empty":
        if len(deque)==0:
            print(1)
        else:
            print(0)
    elif a[0]=="front":
        if len(deque)==0:
            print(-1)
        else:
            print(deque[0])
    elif a[0]=="back":
        if len(deque)==0:
            print(-1)
        else:
            print(deque[-1])
        
