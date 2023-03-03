# 네트워크 - Level 3

def solution(n, computers):    
    
    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])
        return parent[x]
    
    def union(a, b):
        a=find(a)
        b=find(b)

        if a<b:
            parent[b]=a
        else:
            parent[a]=b

    parent=[i for i in range(n+1)]
    
    for i in range(n):
        for j in range(n):
            if i ==j:
                continue
            if computers[i][j]==1:
                print(i+1, j+1)
                union(i+1, j+1)
                
    maps={}
    for i in range(1, n+1):
        v=find(parent[i])
        if not v in maps:
            maps[v]=1

    return len(maps)
