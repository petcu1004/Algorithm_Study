## 도시 분할 계획

import sys
sys.setrecursionlimit(10**6)

input=sys.stdin.readline

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

n, m= map(int, input().split())

parent=[i for i in range(n+1)]

# 간선 정보 담을 리스트와 최소 신장 트리 계산 변수 정의
edges=[]
res=[]

# 간선 정보 주어지고 비용을 기준으로 정렬
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

# 간선 정보 비용 기준으로 오름차순 정렬
edges.sort()

# 간선 정보 하나씩 확인하면서 크루스칼 알고리즘 수행
for e in edges:
    c, a, b = e
    # find 연산 후, 부모 노드 다르면 사이클 발생하지 않으므로 union 연산 수행 -> 최소 신장 트리에 포함!
    if find(a) != find(b):
        union(a, b)
        res.append(c)

print(sum(res[:-1])) #비용이 가장 큰 간선을 지워야 하기 때문에 가장 큰 유지비가 드는 간선 제외하고 유지비의 합을 구함
