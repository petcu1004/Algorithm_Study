## 피로도

from itertools import permutations

def solution(k, dungeons):

    answer=0
    n=len(dungeons)

    for p in permutations(dungeons, n):
        kk=k
        count=0
        for i in p:
            if kk >= i[0]:
                kk-=i[1]
                count+=1
            if count > answer:
                answer=count
                
    return answer