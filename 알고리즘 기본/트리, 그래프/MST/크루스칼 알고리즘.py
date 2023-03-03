import sys

v, e = map(int, input().split())

# 부모 테이블 초기화
parent=[i for i in (1, v+1)]

# find 연산
def find(x):
    if parent[x] !=x:
        parent[x]= find(parent[x])
    return parent[x]

def union(a, b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a] =b

# 간선 정보 담을 리스트와 최소 신장 트리 계산 변수 정의
edges=[]
total_cost=0

# 간선 정보 주어지고 비용을 기준으로 정렬
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

# 간선 정보 비용 기준으로 오름차순 정렬
edges.sort()


# 간선 정보 하나씩 확인하면서 크루스칼 알고리즘 수행
for i in range(e):
    c, a, b = edges[i]
    # find 연산 후, 부모 노드 다르면 사이클 발생하지 않으므로 union 연산 수행 -> 최소 신장 트리에 포함!
    if find(a) != find(b):
        union(a, b)
        total_cost+=total_cost

print(total_cost)