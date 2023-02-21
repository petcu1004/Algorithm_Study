# 네트워크

### BFS
from collections import deque

def solution(n, computers):
    
    def bfs(i):
        q=deque([i]) # 2. 큐에서 가장 앞의 노드(가장 먼저 삽입된 노드)
        while q: # 4. 큐에 원소가 없을 때까지 반복
            i=q.popleft() # 가장 앞에 있는 정점 값이 나옴. pop-> 새 노드

            for a in range(n): # 3. 새 놓드에 대해 1번 반복
                if computers[i][a] and not visited[a]: # 인접하면서 and 방문하지 않음
                    q.append(a) # 큐에 삽입 후, 
                    visited[a]=1 # 방문 체크

    answer = 0
    visited=[0 for i in range(len(computers))] #0으로 초기화하고 방문하면 체크
    
    #1. 현재 노드와 연결된 노드 중 방문되지 않은 모든 노드에 대해 방문체크 후 큐에 삽입
    for i in range(n):
        if not visited[i]: #방문하지 않은 노드들일때,
            bfs(i)
            answer+=1
        
    return answer

### DFS
def solution(n, computers):            
    
    def DFS(i):
        visited[i] = 1 # 방문 체크
        for a in range(n): 
            #computers[i][a]가 1이라면 인접하여 연결된 것이며, 0이며 연결되어있지 않아 인접한 노드가 아닌 것이다.
            if computers[i][a] and not visited[a]: # 인접한가? 확인 and 방문하지 않았나?
                DFS(a) # 현재 노드를 새로 방문한 노드로 변경     
                
    answer = 0
    visited = [0 for i in range(len(computers))] #방문 체크할 리스트 0으로 초기화
    for i in range(n):
        if not visited[i]: # 1. 현재 노드와 연결된 노드 중 하나의 노드 방문 여부 체크
            DFS(i)
            answer += 1
        
    return answer