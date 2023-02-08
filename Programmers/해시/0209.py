#완주하지 못한 선수

from collections import Counter

def solution(participant, completion):
    answer = ''
    
    a=Counter(participant)
    b=Counter(completion)

    res=a-b

    for i in a.keys():
        if(res[i]>=1):
            answer=i


    return answer