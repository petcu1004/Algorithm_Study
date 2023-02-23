## 단어 변환

from collections import deque

def solution(begin, target, words):
    
    def bfs(begin, cnt):
        
        q=deque()
        q.append([begin, 0])
        visited=[0]* len(words)
        while q:
            word, cnt = q.popleft()
            if word == target:
                return cnt
            
            for i in range(len(words)):
                tmp_cnt=0
                if not visited[i]:
                    for j in range(len(word)):
                        if word[j] !=words[i][j]:
                            tmp_cnt+=1
                    if tmp_cnt ==1:
                        q.append([words[i], cnt+1])
                        visited[i]=1

    if target not in words:
        return 0
    
    else:
        answer= bfs(begin, 0)

    return answer