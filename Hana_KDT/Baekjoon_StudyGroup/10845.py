# 큐
import sys
input=sys.stdin.readline

n=int(input())

queue=list()

for i in range(n):
    a=input().split()

    if a[0]=="push":
        queue.append(a[1])
    elif a[0]=="pop":
        if len(queue) ==0:
            print(-1)
        else:
            print(queue[0])
            k=queue[0]
            queue.remove(k)
    elif a[0]=="size":
        print(len(queue))
    elif a[0]=="empty":
        if len(queue) ==0:
            print(1)
        else:
            print(0)
    elif a[0]=="front":
        if len(queue) ==0:
            print(-1)
        else:
            print(queue[0])
            
    elif a[0]=="back":
        if len(queue) ==0:
            print(-1)
        else:
            print(queue[-1])
