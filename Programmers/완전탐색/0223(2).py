## 전력망을 둘로 나누기

from collections import deque

def solution(n, wires):

    def bfs(start):
        visited=[0] * (n+1)
        q=deque([start])
        visited[start]=1
        cnt =1
        while q:
            s = q.popleft()
            for i in graph[s]:
                if not visited[i]:
                    q.append(i)
                    visited[i]=1
                    cnt+=1
        return cnt
    
    
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        #정점에 따라 연결되어있는 점들을 추가해줌
        graph[a].append(b)
        graph[b].append(a)

    res=n
    for a, b in wires: #전선을 하나씩 끊어봄
        graph[a].remove(b)
        graph[b].remove(a)
        
        # 두 쪽 전력망에 속한 송전탐의 개수를 세서 뺀다음 절댓값으로 나온 값 중 가장 작은 값이 답이다.
        res = min(abs(bfs(a) - bfs(b)), res) 
        
        graph[a].append(b)
        graph[b].append(a)

    return res