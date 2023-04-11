# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# def find(x):
#     if parent[x] != x:
#         parent[x]= find(parent[x])
#     return parent[x]

# def union(a, b):
#     a=find(a)
#     b=find(b)
#     #값이 더 작은 것이 부모 노드로 취급함.
#     if a<b:
#         parent[b]=a
#     else:
#         parent[a]=b

# v, e = map(int, input().split())

# parent = [i for i in range(v+1)]


# for _ in range(e):
#     k, a, b = map(int, input().split())
#     if k==0:
#         union(a, b)
#     elif k == 1:
#         if find(a)==find(b):
#             print("YES")
#         else:
#             print("NO")



def find(x):
    if parent[x] !=x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v, e = map(int, input().split())

parent=[i for i in range(v+1)]

for _ in range(e):
    k, a, b = map(int, input().split())
    if k==0:
        union(a, b)
    elif k==1:
        if find(a)==find(b):
            print("YES")
        else:
            print("NO")